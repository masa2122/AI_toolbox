# MediaPipe

 Googleが開発した機械学習と画像処理の機能が搭載されたフレームワーク。
 また、解析をするに当たり数値計算やグラフ表示等を効率的に行うことができる。
 Python を使用する。 iOS やアンドロイドといったスマートフォン用 OS にも対 応しており手軽に使用が可能である。

- Vision tasks
  - Object detection (EfficientDet-Lite, EfficientNet-Lite2, SSDMobileNet-V2) [(URL)](./vision/object_detection.ipynb)
  - Image classification (EfficientNet-Lite0, EfficientNet-Lite2) [(URL)](./vision/classification.ipynb)
  - Image segmentation (SelfieSegmenter, HairSegmenter, SelfieMulticlass, DeepLab-V3) [(URL)](./vision/segmentation.ipynb)
  - Interactive image segmentation (MagicTouch) [(URL)](./vision/interactive_img_segmentation.ipynb)
  - Gesture recognition (GestureRecognizer) [(URL)](./vision/gesture.ipynb)
  - Hand landmarks detection (HandLandmarker) [(URL)](./vision/hand_landmarker.ipynb)
  - Image embedding (MobileNet-V3) [(URL)](./vision/image_embedder.ipynb)
  - Face detection (BlazeFace) [(URL)](./vision/face_detection.ipynb)
  - Face landmark detection (FaceLandmarker) [(URL)](./vision/face_landmark.ipynb)
  - Pose landmark detection (Pose landmarker) [(URL)](./vision/pose_landmarker.ipynb)
- Text tasks
  - Text classification (Average word embedding, BERT-classifier) [(URL)](./text/text_classification.ipynb)
  - Text embedding (Universal Sentence Encoder) [(URL)](./text/text_embed.ipynb)
  - Language detection (Language Detector) [(URL)](./text/language_detection.ipynb)
- Audio tasks
  - Audio classification (YamNet) [(URL)](./audio/audio_classification.ipynb)

## References
- https://developers.google.com/mediapipe

## Memo
mp.tasks＝元
mp.solutions＝↑を利用した技術

↓solutions
https://github.com/google/mediapipe/tree/master/docs/solutions