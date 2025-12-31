# Real-Time American Sign Language Recognition Using 3D Convolutional Neural Networks and LSTM: Architecture, Training, and Deployment

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2512.22177)

## 요약
arXiv:2512.22177v1 Announce Type: new
Abstract: This paper presents a real-time American Sign Language (ASL) recognition system utilizing a hybrid deep learning architecture combining 3D Convolutional Neural Networks (3D CNN) with Long Short-Term Memory (LSTM) networks. The system processes webcam video streams to recognize word-level ASL signs, addressing communication barriers for over 70 million deaf and hard-of-hearing individuals worldwide. Our architecture leverages 3D convolutions to capture spatial-temporal features from video frames, followed by LSTM layers that model sequential dependencies inherent in sign language gestures. Trained on the WLASL dataset (2,000 common words), ASL-LEX lexical database (~2,700 signs), and a curated set of 100 expert-annotated ASL signs, the system achieves F1-scores ranging from 0.71 to 0.99 across sign classes. The model is deployed on AWS infrastructure with edge deployment capability on OAK-D cameras for real-time inference. We discuss the architecture design, training methodology, evaluation metrics, and deployment considerations for practical accessibility applications.
