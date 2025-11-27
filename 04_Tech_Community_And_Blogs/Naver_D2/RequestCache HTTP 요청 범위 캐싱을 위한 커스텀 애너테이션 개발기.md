# @RequestCache: HTTP 요청 범위 캐싱을 위한 커스텀 애너테이션 개발기

**출처:** [Naver_D2](https://d2.naver.com/helloworld/7610642)

## 요약
웹 애플리케이션을 개발하다 보면 하나의 HTTP 요청 내에서 동일한 외부 API를 여러 번 호출하거나 동일한 연산을 반복하는 경우가 종종 발생합니다. 이러한 중복 호출은 응답 시간을 증가시키고 불필요한 네트워크 오버헤드를 유발합니다.

이 글에서는 이러한 문제를 해결하기 위해 개발한 `@RequestCache`라는 커스텀 애너테이션의 개발 과정과 그 과정에서 겪은 시행착오를 공유하고자 합니다.

@RequestCache 소개
----------------

다음과 같은 서비스 구조를 가정해 보겠습니다.

![](https://d2.naver.com/content/images/2025/11/1-1.png)

위 구조에서 `OrderValidationService`, `PaymentService`, `NotificationService` 각각에서 사용자의 프로필 정보가 필요하다면, 세 서비스 모두 프로필 조회 API를 호출합니다. 이러한 중복 호출은 **응답 시간 증가**, **외부 서버의 부하**, **리소스 낭비** 등의 문제를 야기합니다.

이러한 문제를 해결하기 위해 @RequestCache를 개발했습니다. `@RequestCache`는 **HTTP 요청 범위(request scope) 내에서 메서드의 호출 결과를 캐싱**하는 Spring 기반의 커스텀 애너테이션입니다. 하나의 HTTP 요청 내에서 중복된 외부 API 호출이나 반복적인 연산을 방지하여 성능을 개선할 수 있습니다.

`@RequestCache`는 다음과 같은 특징이 있습니다.

* **RequestAttribute 기반의 캐시 저장**: `RequestAttribute`를 사용하여 요청별로 독립적인 캐시 인스턴스를 보장합니다. `RequestAttribute`는 내부에서 ThreadLocal을 사용하므로 각 스레드의 인스턴스가 독립적이며 스레드 간 격리가 보장됩니다.
* **자동 생명주기 관리**: 캐시와 HTTP 요청의 생명주기가 같으므로 별도로 TTL(time to live)을 관리할 필요가 없습니다. 요청 처리 완료 시 Spring의 `FrameworkServlet`이 자동으로 `RequestAttribute`를 정리해 메모리 누수를 방지합니다.
* **간편한 사용법**: 애너테이션 하나로 손쉽게 메서드 호출 결과를 캐싱할 수 있습니다.

다음과 같이 `@RequestCache`를 선언하면, 하나의 HTTP 요청 내에서 같은 `userId`로 `findProfileByUserId()`을 여러 번 호출하는 경우에 실제 외부 API는 한 번만 호출되고 이후에는 캐시된 결과가 반환됩니다.

```
@Service
@RequiredArgsConstructor
public class ProfileService {  
    private final ProfileApiClient profileApiClient;

    @RequestCache(cacheNames = "findProfileByUserId")
    public Profile findProfileByUserId(Long userId) {
        // 외부 API 호출
        return profileApiClient.findProfileByUserId(userId);
    }
}
```

대안 검토
-----

본격적인 개발에 앞서 `@RequestCache`가 정말 필요한지 검증하기 위해 다음 두 가지 대안을 검토했습니다.

* 응답 객체를 파라미터로 계속 넘겨주기
* Redis/Local 캐시를 사용하고 TTL을 적절하게 설정하기

### 응답 객체를 파라미터로 넘기는 방식의 한계

첫 번째 대안은 응답 객체를 메서드 파라미터로 계속 전달하는 것입니다. 하지만 이 방식은 다음과 같은 문제점이 있습니다.

#### 호출 깊이가 깊은 경우

```
@RestController
@RequiredArgsConstructor
public class TransactionController {  
    private final OrderValidationService orderValidationService;
    private final PaymentService paymentService;
    private final NotificationService notificationService;
    private final ProfileService profileService;

    @PostMapping("/order")
    public void processOrder(@RequestParam Long orderId, @RequestParam Long userId) {
        Profile profile = profileService.getProfile(userId);

        // ... 주문 검증 Profile 전달
        orderValidationService.validate(orderId, profile);

        paymentService.purchase(orderId, profile);
        notificationService.noti(orderId, profile);
    }
}

@Service
@RequiredArgsConstructor
public class OrderValidationService {  
    private final DeliveryValidator deliveryValidator;

    public void validate(Long orderId, Profile profile) {
        // ... 주문 검증 로직 (Profile 미사용)

        deliveryValidator.validateDeliveryArea(orderId, profile);  // Profile 전달
    }
}

@Service
@RequiredArgsConstructor
public class DeliveryValidator {  
    private final PricingCalculator pricingCalculator;

    public void validateDeliveryArea(Long orderId, Profile profile) {
        // ... 배송 지역 검증 로직 (Profile 미사용)
        Money fee = pricingCalculator.calculateFee(orderId, profile);  // Profile 전달
        // ... 배송비 검증
    }
}

@Service
@RequiredArgsConstructor
public class PricingCalculator {

    public Money calculateFee(Long orderId, Profile profile) {
        // 실제로 Profile을 사용하는 곳은 여기뿐
        if (profile.isPremiumMember()) {
            return Money.ZERO;
        }
        return Money.of(3000);
    }
}
```

이 코드에서 실제로 `Profile`을 사용하는 곳은 `PricingCalculator.calculateFee()` 메서드뿐입니다. 하지만 이 데이터를 전달하기 위해 `OrderValidationService` → `DeliveryValidator` → `PricingCalculator`의 모든 메서드가 Profile 파라미터를 선언해야 합니다.

즉, 응답 객체를 파라미터로 넘기는 방식은 호출 깊이가 깊은 경우에 다음과 같은 문제가 있습니다.

* 중간 계층(`OrderValidationService`, `DeliveryValidator`)은 응답 객체를 사용하지 않지만 파라미터로 받아야 함
* 호출 깊이가 깊어질수록 파라미터 전달이 복잡해짐
* 새로운 데이터가 필요할 때마다 모든 메서드 시그니처를 수정해야 함

#### 전략 패턴을 사용하는 경우

```
public interface DiscountPolicy {  
    Money calculate(Long orderId, Profile profile);
}

@Component
public class MemberGradeDiscountPolicy implements DiscountPolicy {  
    @Override
    public Money calculate(Long orderId, Profile profile) {
        // Profile의 등급 정보를 사용
        return switch (profile.getGrade()) {
            case GOLD -> Money.of(5000);
            case SILVER -> Money.of(3000);
            default -> Money.ZERO;
        };
    }
}

@Component
public class CouponDiscountPolicy implements DiscountPolicy {  
    private final CouponRepository couponRepository;

    @Override
    public Money calculate(Long orderId, Profile profile) {
        // Profile을 사용하지 않지만 인터페이스 때문에 선언해야 함
        return couponRepository.findByOrderId(orderId)
            .map(Coupon::getDiscountAmount)
            .orElse(Money.ZERO);
    }
}
```

인터페이스에 Profile을 추가하면, 실제로 Profile이 필요하지 않은 `CouponDiscountPolicy`도 Profile을 파라미터로 받아야 합니다. 이는 불필요한 의존성을 만들고 인터페이스의 유연성을 해칩니다.

즉, 파라미터 전달 방식은 호출 깊이가 깊거나 전략 패턴을 사용하는 경우에 적용하기 어렵습니다.

### Redis/Local 캐시의 TTL 설정 딜레마

두 번째 대안은 Redis나 Local 캐시를 사용하고 적절한 TTL을 설정하는 것입니다. 하지만 이 방식도 다음과 같은 문제가 있습니다.

#### TTL이 너무 짧은 경우

TTL이 너무 짧으면, 하나의 요청 내에서 같은 데이터를 두 번 조회하는 경우에 두 번째 조회 시 첫 번째 캐시가 만료되어 다시 API를 호출해야 합니다. 이는 중복 호출을 방지하려는 원래 목적을 달성하지 못합니다.

![](https://d2.naver.com/content/images/2025/11/2-1.png)

예를 들어, 요청 처리 시간이 5초인데 TTL을 3초로 설정한 경우 다음과 같이 동작합니다.

```
Request A 시작(0초)  
├─ Profile 조회(0.1초) - 캐시 미스, 캐시에 저장(3초 후 만료)
├─ 비즈니스 로직 처리(0.1~3.5초)
├─ Profile 조회(3.5초) - TTL 만료로 캐시 미스(중복 호출 발생)
└─ Request A 종료(5초)
```

#### TTL이 너무 긴 경우

TTL을 길게 설정해도 만료 시점에 따라 캐시 효과가 불안정합니다.

![](https://d2.naver.com/content/images/2025/11/3-1.png)

요청 B는 요청 A에서 생성된 캐시를 사용합니다. @RequestCache의 목적은 동일 요청 내 중복 호출 방지이므로, 논리적으로 서로 다른 요청 간에 캐시를 공유하는 것은 의도하지 않은 동작입니다. 요청 C에서는 캐시가 만료되어 다시 캐시 미스가 발생합니다.

예를 들어, 요청 처리 시간이 3초인데 TTL을 10초로 설정한 경우 다음과 같이 동작합니다.

```
요청 A 시작(0초)
├─ Profile 조회(0.5초) - 캐시 미스, 캐시에 저장(10초 후 만료)
└─ 요청 A 종료(3초)

요청 B 시작(5초)
├─ Profile 조회(5.5초) - 캐시 적중(요청 A의 캐시 사용)
└─ 요청 B 종료(8초)

요청 C 시작(11초)
├─ Profile 조회(11.5초) - 캐시 미스(요청 A의 캐시 만료)
└─ 요청 C 종료(14초)
```

즉, 적절한 TTL을 설정하기 어려우므로 Redis/Local 캐시는 HTTP 요청 범위 캐싱에 적합하지 않으며, 요청 범위와 일치하는 생명주기의 캐시가 필요하다는 결론에 도달했습니다.

@RequestScope를 이용한 첫 번째 시도
--------------------------

Spring의 `@RequestScope`는 Bean의 생명주기를 HTTP 요청 범위로 설정합니다. 이를 CacheManager에 적용하면 간단하게 요청별 캐싱을 구현할 수 있을 것 같았습니다.

```
@Config
public class CacheConfig {  
    @Bean
    @RequestScope
    public CacheManager requestCacheManager() {
        return new ConcurrentMapCacheManager();
    }
}
```

### @RequestScope의 동작 원리

`@RequestScope`를 제대로 이해하고 사용하기 위해서는 먼저 다음 두 가지 의문점을 해결해야 했습니다.

* @RequestScope Bean은 어떻게 요청마다 다른 인스턴스를 사용할까?
* @RequestScope를 붙이면 요청별로 완전히 분리될까?

#### Proxy 패턴을 통한 요청별 인스턴스 관리

첫 번째 의문의 핵심은 **Proxy**였습니다.

![](https://d2.naver.com/content/images/2025/11/4-1.png)

`@RequestScope`로 선언된 Bean은 Spring Container에 Proxy 객체로 등록됩니다. 이 Proxy는 싱글턴으로 관리되지만, 실제 메서드 호출 시 현재 요청에 해당하는 실제 인스턴스를 조회하여 메서드 호출을 위임합니다. 각 HTTP 요청마다 새로운 실제 인스턴스가 생성되어 사용됩니다.

#### RequestAttribute를 통한 요청별 분리와 자동 정리

두 번째 의문에 대한 답은 Spring의 `AbstractRequestAttributesScope` 클래스를 살펴보면 알 수 있습니다.

```
// AbstractRequestAttributesScope.class
public abstract class AbstractRequestAttributesScope implements Scope {

    @Override
    public Object get(String name, ObjectFactory<?> objectFactory) {
        RequestAttributes attributes = RequestContextHolder.currentRequestAttributes();
        Object scopedObject = attributes.getAttribute(name, this.getScope());
        if (scopedObject == null) {
            scopedObject = objectFactory.getObject();
            attributes.setAttribute(name, scopedObject, this.getScope());
            Object retrievedObject = attributes.getAttribute(name, this.getScope());
            if (retrievedObject != null) {
                scopedObject = retrievedObject;
            }
        }

        return scopedObject;
    }
}
```

`@RequestScope` Bean의 실제 인스턴스는 `RequestAttribute`에 저장됩니다. `RequestAttribute`는 `FrameworkServlet`에서 생성되므로 요청별로 완전히 분리됩니다. 또한 내부에서 `ThreadLocal`을 사용해 thread-safe를 보장합니다.

RequestAttribute의 자동 정리 메커니즘에 대해서 좀 더 자세히 알아보겠습니다. `RequestAttribute`에 저장된 데이터는 요청 종료 시 자동으로 정리되는데, 이는 `FrameworkServlet`의 `processRequest()` 메서드에서 보장됩니다.

```
// FrameworkServlet.class
public abstract class FrameworkServlet extends HttpServletBean {

    protected final void processRequest(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        long startTime = System.currentTimeMillis();
        Throwable failureCause = null;
        LocaleContext previousLocaleContext = LocaleContextHolder.getLocaleContext();
        LocaleContext localeContext = this.buildLocaleContext(request);
        RequestAttributes previousAttributes = RequestContextHolder.getRequestAttributes();
        ServletRequestAttributes requestAttributes = this.buildRequestAttributes(request, response, previousAttributes);
        WebAsyncManager asyncManager = WebAsyncUtils.getAsyncManager(request);
        asyncManager.registerCallableInterceptor(FrameworkServlet.class.getName(), new RequestBindingInterceptor());
        this.initContextHolders(request, localeContext, requestAttributes);

        try {
            this.doService(request, response);
        } catch (IOException | ServletException ex) {
            failureCause = ex;
            throw ex;
        } catch (Throwable ex) {
            failureCause = ex;
            throw new ServletException("Request processing failed: " + ex, ex);
        } finally {
            this.resetContextHolders(request, previousLocaleContext, previousAttributes);
            if (requestAttributes != null) {
                requestAttributes.requestCompleted();
            }

            this.logResult(request, response, failureCause, asyncManager);
            this.publishRequestHandledEvent(request, response, startTime, failureCause);
        }
    }
}
```

`finally` 블록에서 `requestAttributes.requestCompleted()`를 호출하여, 요청이 정상 종료되든 예외가 발생하든 관계없이 RequestAttribute가 반드시 정리됩니다. 그 결과 메모리 누수가 방지됩니다.

### Spring Actuator와의 충돌

`@RequestScope`를 적용하고 애플리케이션을 실행하자 예상치 못한 문제가 발생했습니다. `ScopeNotActiveException`이 발생해 애플리케이션이 실행되지 않았습니다.

![](https://d2.naver.com/content/images/2025/11/5-1.png)

```
Error creating bean with name 'cacheManager': Scope 'request' is not active  
for the current thread; consider defining a scoped proxy for this bean
```

#### 오류 발생 원인

원인은 Spring Actuator의 `CacheMetricsAutoConfiguration`과의 충돌이었습니다. `CacheMetricsAutoConfiguration`은 애플리케이션 시작 시점에 실행되는데, 이때는 HTTP 요청이 없어 `RequestScope`가 활성화되지 않습니다.

오류가 발생하는 전체 흐름은 다음과 같습니다.

`@RequestScope` Bean의 Proxy가 실제 타겟 객체를 resolve하기 위해 `Scope` 인터페이스의 `get()` 메서드를 호출합니다. `@RequestScope`의 경우 `AbstractRequestAttributesScope.get()`이 호출됩니다. 이때 `RequestContextHolder.currentRequestAttributes()`가 호출됩니다.

```
// AbstractRequestAttributesScope.class
public abstract class AbstractRequestAttributesScope implements Scope {

    public Object get(String name, ObjectFactory<?> objectFactory) {
        RequestAttributes attributes = RequestContextHolder.currentRequestAttributes();
        ...
    }
}
```

`currentRequestAttributes()` 메서드에서 HTTP 요청이 활성화되지 않은 경우 `IllegalStateException`이 발생합니다.

```
// RequestContextHolder.class
public abstract class RequestContextHolder {

    public static RequestAttributes currentRequestAttributes() throws IllegalStateException {
        RequestAttributes attributes = getRequestAttributes();
        if (attributes == null) {
            if (jsfPresent) {
                attributes = RequestContextHolder.FacesRequestAttributesFactory.getFacesRequestAttributes();
            }
            if (attributes == null) {
                // HTTP 요청이 활성화되지 않은 경우
                throw new IllegalStateException(
                    "No thread-bound request found:...");
            }
        }
        return attributes;
    }
}
```

`AbstractBeanFactory`에서 이를 catch하여 `ScopeNotActiveException`을 던집니다.

```
// AbstractBeanFactory.class
public abstract class AbstractBeanFactory extends FactoryBeanRegistrySupport  
    implements ConfigurableBeanFactory {

    protected <T> T doGetBean(String name, ...) throws BeansException {
        ...
        catch (IllegalStateException ex) {
            throw new ScopeNotActiveException(beanName, scopeName, ex);
        }
        ...
    }
}
```

#### 임시 해결책 및 한계

`CacheMetricsAutoConfiguration`을 제외하면 기술적으로는 동작하지만 캐시 적중/미스와 같은 중요한 메트릭을 수집할 수 없습니다.

```
@Config
@EnableAutoConfiguration(exclude = {CacheMetricsAutoConfiguration.class})
public class CacheConfig {  
    @Bean
    @RequestScope
    public CacheManager requestCacheManager() {
        return new ConcurrentMapCacheManager();
    }
}
```

이는 근본적인 해결책이 아니므로 다른 방식을 고민했습니다.

최종 해결책: 커스텀 CacheManager
------------------------

`@RequestScope` 방식은 `RequestAttribute`에 `CacheManager` 인스턴스를 저장하므로 애플리케이션 시작 시점에 resolve를 시도해 오류가 발생했습니다. 이 과정에서 얻은 인사이트를 바탕으로, 다음과 같은 커스텀 방식을 설계했습니다.

* `CacheManager` 자체는 싱글턴으로 유지
* `RequestAttribute`에 **Cache 객체**를 저장
* HTTP 요청 활성화 여부를 확인해 적절히 처리

![](https://d2.naver.com/content/images/2025/11/6-2.png)

커스텀 방식은 `RequestAttribute`에 Cache 객체를 저장하므로, 애플리케이션 시작 시점에는 `CacheManager`만 사용해 오류가 발생하지 않습니다.

### 1. 커스텀 CacheManager 구현

이러한 커스텀 방식을 구현하기 위해서는 Spring의 `CacheManager` 인터페이스를 직접 구현해야 합니다.

![](https://d2.naver.com/content/images/2025/11/7-2.png)

#### HTTP 요청 컨텍스트 활성화 확인

먼저, HTTP 요청이 활성화되어 있는지 확인하는 유틸리티 메서드를 구현합니다.

```
// RequestScopedCacheManager.class

private boolean isRequestContextActive() {  
    try {
        RequestContextHolder.currentRequestAttributes();
        return true;
    } catch (IllegalStateException e) {
        // HTTP 요청이 활성화되지 않은 경우
        return false;
    }
}
```

앞에서 본 것처럼 `IllegalStateException`이 발생하면 요청이 활성화되지 않은 것으로 판단합니다.

#### 핵심 로직 getCache() 구현

`RequestScopedCacheManager`의 핵심은 `getCache()` 구현입니다. `CacheManager`의 `getCache()` 메서드는 주어진 이름에 해당하는 캐시를 반환하는 역할을 합니다. `@Cacheable` 등의 애너테이션이 동작할 때 캐시를 가져오기 위해 이 메서드를 사용합니다.

```
// RequestScopedCacheManager.class

@Override
public Cache getCache(String name) {  
    try {
        // 1. 요청 컨텍스트 활성화 확인
        if (!isRequestContextActive()) {
            return new NoOpCache(name);
        }

        // 2. RequestAttribute에서 캐시 조회
        RequestAttributes requestAttributes = RequestContextHolder.currentRequestAttributes();
        String cacheKey = CACHE_ATTRIBUTE_PREFIX + name;
        Cache cache = (Cache)requestAttributes.getAttribute(cacheKey, RequestAttributes.SCOPE_REQUEST);

        // 3. 캐시가 없으면 생성 후 RequestAttribute에 저장
        if (cache == null) {
            cache = createNewCache(name);
            requestAttributes.setAttribute(cacheKey, cache, RequestAttributes.SCOPE_REQUEST);
        }

        return cache;
    } catch (Exception e) {
        log.warn("요청 캐시 조회 실패 - 캐시 비활성화", e);
        return new NoOpCache(name);
    }
}
```

동작 흐름은 다음과 같습니다.

1. **요청 컨텍스트 활성화 확인**: HTTP 요청이 활성화되지 않은 경우 `NoOpCache` 반환
2. **RequestAttribute에서 캐시 조회**: 요청별로 저장된 캐시 조회
3. **캐시 생성 및 저장**: 캐시가 없으면 새로 생성해 RequestAttribute에 저장
4. **예외 처리**: 예상치 못한 오류 발생 시에도 `NoOpCache`를 반환해 안전하게 처리

1번 과정에서 `null` 대신 `NoOpCache`를 반환하는 이유를 알아보겠습니다.

Spring의 `CacheManager` 인터페이스 명세를 보면 `getCache()` 메서드는 캐시가 없거나 생성할 수 없을 때 `null`을 반환하도록 정의되어 있습니다.

![](https://d2.naver.com/content/images/2025/11/8-2.png)

하지만 실제로 `null`을 반환하면 Spring의 `AbstractCacheResolver`에서 오류가 발생합니다.

```
// AbstractCacheResolver.class
public abstract class AbstractCacheResolver implements CacheResolver {

    @Override
    public Collection<? extends Cache> resolveCaches(CacheOperationInvocationContext<?> context) {
        Collection<String> cacheNames = getCacheNames(context);
        if (cacheNames == null) {
            return Collections.emptyList();
        }
        Collection<Cache> result = new ArrayList<>(cacheNames.size());
        for (String cacheName : cacheNames) {
            Cache cache = getCacheManager().getCache(cacheName);
            if (cache == null) {
                // null을 반환하면 여기서 예외 발생!
                throw new IllegalArgumentException("Cannot find cache named '" +
                    cacheName + "' for " + context.getOperation());
            }
            result.add(cache);
        }
        return result;
    }
}
```

`AbstractCacheResolver`는 `@Cacheable`, `@CacheEvict` 등의 애너테이션에서 어떤 캐시를 사용할지 결정하는 클래스입니다. 이 클래스는 `getCache()`가 `null`을 반환하면 `IllegalArgumentException`을 던집니다.

이를 방지하기 위해 Spring의 `NoOpCache`를 반환합니다. `NoOpCache`는 캐싱을 수행하지 않는 더미 구현체로, 요청 컨텍스트가 비활성화된 환경에서도 오류 없이 정상 동작하도록 합니다. 단, 실제 캐싱은 되지 않으므로 매번 메서드가 실행됩니다.

```
// NoOpCache.class
public class NoOpCache implements Cache {

    private final String name;

    @Override
    public ValueWrapper get(Object key) {
        return null; // 항상 캐시 미스
    }

    @Override
    public void put(Object key, Object value) {
        // 아무 동작도 하지 않음
    }

    // ... 나머지 메서드도 모두 no-op
}
```

#### 전체 구현 코드

`RequestScopedCacheManager`의 전체 코드는 다음과 같습니다.

```
// RequestScopedCacheManager.class
public class RequestScopedCacheManager implements CacheManager {

    private static final String CACHE_ATTRIBUTE_PREFIX = "requestCache.";

    @Override
    public Cache getCache(String name) {
        try {
            if (!isRequestContextActive()) {
                return new NoOpCache(name);
            }

            RequestAttributes requestAttributes = RequestContextHolder.currentRequestAttributes();
            String cacheKey = CACHE_ATTRIBUTE_PREFIX + name;
            Cache cache = (Cache)requestAttributes.getAttribute(cacheKey, RequestAttributes.SCOPE_REQUEST);

            if (cache == null) {
                cache = createNewCache(name);
                requestAttributes.setAttribute(cacheKey, cache, RequestAttributes.SCOPE_REQUEST);
            }

            return cache;
        } catch (Exception e) {
            log.warn("요청 캐시 조회 실패 - 캐시 비활성화", e);
            return new NoOpCache(name);
        }
    }

    @Override
    public Collection<String> getCacheNames() {
        if (!isRequestContextActive()) {
            return Collections.emptyList();
        }
        return Collections.singletonList("requestCache");
    }

    private Cache createNewCache(String name) {
        return new ConcurrentMapCache(name, new ConcurrentHashMap<>(), false);
    }

    private boolean isRequestContextActive() {
        try {
            RequestContextHolder.currentRequestAttributes();
            return true;
        } catch (IllegalStateException e) {
            // HTTP 요청이 활성화되지 않은 경우
            return false;
        }
    }
}
```

### 2. @RequestCache 애너테이션 생성

이제 사용 편의성을 위해 커스텀 애너테이션을 만들겠습니다. `@Cacheable`을 메타 애너테이션으로 사용해 Spring의 기존 캐싱 기능을 그대로 활용하면서, 앞에서 개발한 커스텀 CacheManager를 `cacheManager`에 지정합니다.

```
@Target({ElementType.TYPE, ElementType.METHOD})
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Cacheable(cacheManager = "requestScopedCacheManager")
public @interface RequestCache {

    @AliasFor(annotation = Cacheable.class, attribute = "value")
    String[] value() default {"requestCache"};

    @AliasFor(annotation = Cacheable.class, attribute = "cacheNames")
    String[] cacheNames() default {"requestCache"};

    @AliasFor(annotation = Cacheable.class, attribute = "condition")
    String condition() default "";

    @AliasFor(annotation = Cacheable.class, attribute = "unless")
    String unless() default "#result == null";
}
```

### 3. Bean 등록

일반적인 싱글턴 Bean으로 등록하며, `@EnableCaching`으로 Spring의 캐싱 기능을 활성화합니다.

```
@Configuration
@EnableCaching
public class CacheConfig {

    @Bean
    public CacheManager requestScopedCacheManager() {
        return new RequestScopedCacheManager();
    }
}
```

### 4. 사용 예

애너테이션까지 만들었으면 다음과 같이 간편하게 사용할 수 있습니다.

```
@Service
@RequiredArgsConstructor
public class ProfileService {  
    private final ProfileApiClient profileApiClient;

    @RequestCache(cacheNames = "findProfileByUserId")
    public Profile findProfileByUserId(Long userId) {
        // 외부 API 호출
        return profileApiClient.findProfileByUserId(userId);
    }
}
```

동작 검증
-----

실제 동작을 검증하기 위해 동일한 요청 내에서 4번 호출하는 테스트를 수행했습니다.

```
@Override
public void findByProfileId(ProfileId profileId) {  
    accountReadPort.findByProfileId(profileId);
    accountReadPort.findByProfileId(profileId); // requestCache
    accountReadPort.findByProfileId(profileId); // requestCache
    accountReadPort.findByProfileId(profileId); // requestCache
}
```

### 첫 번째 호출 결과

`cache`가 `null`인 것과 캐시 생성 로직이 실행되는 것을 확인했습니다.

![](https://d2.naver.com/content/images/2025/11/9-2.png)

### 두 번째 이후 호출 결과

하나의 요청 내에서 두 번째 호출부터는 `RequestAttribute`에 저장된 캐시를 가져와 사용해 실제로 중복 호출이 방지되는 것을 확인했습니다.

![](https://d2.naver.com/content/images/2025/11/10-1.png)

한계점
---

`@RequestCache`는 요청 컨텍스트 기반으로 동작하기 때문에 다음과 같은 한계가 있습니다.

### @Async 메서드에서 사용 불가

`@Async`로 선언된 비동기 메서드는 별도의 스레드에서 실행됩니다. `RequestContextHolder`는 전파 모드를 제공하지만, FrameworkServlet에서 `inheritable`을 `false`로 설정하기 때문에 자식 스레드로 전파되지 않습니다. 따라서 비동기 메서드에서 `@RequestCache`를 사용하면 캐싱이 동작하지 않으며, 오류가 발생하지는 않지만 매번 실제 메서드가 실행됩니다.

### Kafka Consumer에서 사용 불가

Kafka Consumer는 HTTP 요청 컨텍스트가 아닌 메시지 처리 컨텍스트에서 실행됩니다. 따라서 `@RequestCache`를 적용해도 캐싱이 동작하지 않으며, 매번 실제 로직이 수행됩니다.

### 고려했던 대안: ThreadLocal

요청 컨텍스트의 한계를 극복하기 위해 ThreadLocal 방식도 고려해 보았습니다. ThreadLocal을 사용하면 각 스레드의 캐시가 독립적이므로 @Async나 Kafka Consumer 환경에서도 동작할 수 있습니다.

하지만 ThreadLocal 방식은 다음과 같은 문제점이 있어 채택하지 않았습니다.

#### 복잡한 생명주기 관리

ThreadLocal에 저장된 캐시는 자동으로 정리되지 않기 때문에, HTTP 요청, Kafka 메시지 처리 등 각 생명주기마다 수동으로 `clear()`를 호출해야 합니다. AOP나 Interceptor를 통한 자동 정리가 필요하지만, 모든 케이스를 커버하기 어렵습니다. 각 실행 컨텍스트(HTTP 요청, Kafka Consumer, @Async 등)마다 정리 로직을 구현해야 하며, 테스트 환경에서도 별도의 정리 로직이 필요합니다. 이는 코드의 복잡도를 크게 증가시킵니다.

#### 메모리 누수 위험

실수로 캐시를 정리하지 않으면 ThreadLocal에 캐시가 계속 남아 메모리 누수가 발생합니다. 특히 스레드 풀을 사용하는 환경에서는 스레드가 재사용되면서 이전 작업의 캐시가 남아있어 더욱 심각한 문제가 될 수 있습니다.

따라서 `@Async`와 Kafka Consumer에서는 캐싱이 되지 않더라도, 비교적 간단하고 안전한 요청 컨텍스트 방식을 채택했습니다.

마치며
---

`@RequestCache`는 HTTP 요청 범위 캐싱이라는 특정 문제를 해결하기 위해 만들어졌습니다. 완벽하지는 않지만, 실용적이고 안전한 해결책이 되었다고 생각합니다.

혹시 이 글을 읽으신 분 중에 `@Async`나 Kafka Consumer 환경에서도 안전하게 동작하는 더 나은 아이디어가 있는 분이 계시다면, 언제든지 의견을 주시면 감사하겠습니다!
