# FaceRec

深度學習人臉辨識技術

0. 基礎: 機器學習/深度學習/圖形處理器技術

1. "DeepFace: Closing the Gap to Human-Level Performance in Face Verification"

https://www.cv-foundation.org/openaccess/content_cvpr_2014/papers/Taigman_DeepFace_Closing_the_2014_CVPR_paper.pdf?spm=5176.100239.blogcont55892.18.pm8zm1&file=Taigman_DeepFace_Closing_the_2014_CVPR_paper.pdf

*最早的深度學習人臉辨識

*已經有　metric learning 的觀念 (使用 siamese network)

*無權值共享的 CNN => 過多的參數

*3D alignment => 過度複雜


2. "Deep Face Recognition" 

http://cis.csuohio.edu/~sschung/CIS660/DeepFaceRecognition_parkhi15.pdf

*著名的 VGG Face, 整套流程包含 face dataset 的建立

2. (A) "Very deep convolutional networks for large-scale image recognition. In International Conference on Learning Representations"

https://arxiv.org/pdf/1409.1556/

*著名的 VGG Network


3. "FaceNet: A Unified Embedding for Face Recognition and Clustering"

https://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Schroff_FaceNet_A_Unified_2015_CVPR_paper.pdf

*用 triplet loss 產生 128 維的 FaceNet embeddings (此向量空間內的距離代表人臉的相似程度), LFW 準確度超過 99%
 
A. "Labeled Faces in the Wild: A Database for Studying Face Recognition in Unconstrained Environments"

*著名的 lfw 人臉辨識準確率測試資料集
