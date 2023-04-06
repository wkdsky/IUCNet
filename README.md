# IUCNet
This project is an open source experimental project of "IUCNet: A Novel Semantic Segmentation Network for Overlapping Industrial Parts Detection" based on MMsegemantaion scaffolding.
The README (Original) is the official self-contained version.
The path where the home-made dataset of the paper is stored is: ". \data\mydata".

The models involved in the experiments of this project include:
1. DeepLabV3 (ResNet101). Configuration files: ". \configs\deeplabv3\deeplabv3_r101b-d8_*.py"
2. DeepLabV3(MobileNetV2). Configuration file: ". \configs\mobilenet_v2\deeplabv3_m-v2-d8_*.py"
3. DeepLabV3 (UNet). Configuration file: ". \configs\unet\deeplabv3_unet_s5-d16_*.py"
4. DeepLabV3plus (ResNet101). Configuration file: ". \configs\deeplabv3plus\deeplabv3plus_r101-d8_*.py"
5. DeepLabV3plus (MobileNetV2). Configuration file: ". \configs\mobilenet_v2\deeplabv3plus_m-v2-d8_*.py"
6. UperNet (ResNet101). Configuration file: ". \configs\upernet\upernet_r101_512x512_*.py"
7. UperNet (ConvNeXt-Base).  Configuration file: ". \configs\convnext\upernet_convnext_base_fp16_*.py"
8. UperNet (ConvNeXt-Large). Configuration file: ". \configs\convnext\upernet_convnext_large_fp16_640x640_160k_ade20k.py"
9. UperNet (ConvNeXt-Tiny). Configuration file: ". \configs\convnext\upernet_convnext_tiny_fp16_512x512_160k_ade20k.py"
10. GCNet (ResNet101).  Configuration file: ". \configs\gcnet\gcnet_r101-d8_512x512_*.py"
11. K-Net + DeepLabV3 (ResNet50). Configuration file: ". \configs\knet\knet_s3_deeplabv3_r50-d8_8x2_512x512_adamw_80k_ade20k.py"
12. K-Net + UperNet (ResNet50) Configuration file: ". \configs\knet\knet_s3_upernet_r50-d8_8x2_512x512_adamw_80k_ade20k.py"

Experimental run description:
1. configure the dataset read parameters via ". \configs\_base_\datasets\drive.py" to set.
2. configure the model reading parameters, set in the above configuration file, when no specific file is specified, please pay attention to the similarities and differences of the parameters in the file, and pay attention to the consistency of the experiment.
3. For the configuration of the loss function, please set it in the model configuration file (the file pointed to in the read parameters file, usually located in ". \configs\_base_\models"), please change the loss_decode related configuration in the decode_head and auxiliary_head fields.
4. For photometric distortion related configuration, please add dict(type='PhotoMetricDistortion', *) field under the train_pipeline field in the model configuration file.
5. run by the command "python tools/train.py model read file path --work-dir work save path".
