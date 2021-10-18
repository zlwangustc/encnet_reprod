
# EncNet复现
网络原因，部分文件未上传，完整文件保存在baidudisk, 链接：[https://pan.baidu.com/s/1ePgeu-fWRBRs9Xmfrx-wCQ](https://pan.baidu.com/s/1ePgeu-fWRBRs9Xmfrx-wCQ)
提取码：f51e
## 文件结构:
```
encnet_reprod
     ├──  diff # reprod_log的产生的结果
        ├── log # 对比产生的diff.log文件
        ├── model # 对齐的模型权重
        ├── npy # 对比产生的diff.npy文件
        ├── check_log_diff.py
        ├── gen_fake_data.py # 产生fake_data和fake_label
     ├──  encnet_paddle # encnet_Paddle
        ├── config
            ├── encnet
                ├── encnet_cityscapes.yml # 配置文件
        ├── Paddleseg
            ├── models
                ├── backbones
                    ├── resnet_w.py # 复现的主干网络
                ├── losses
                    ├── se_loss.py # 损失函数
                ├── encnet.py # encnet代码
        ├──  train.py  # 训练入口文件
        ├──  predict.py # 预测文件
     ├──  PyTorch-Encoding-master # encnet_Pytorch
     ├── log  # 完整的模型训练评估日志

```

## 复现说明
* 本次复现的encnet原pytorch代码[https://github.com/zhanghang1989/PyTorch-Encoding](https://github.com/zhanghang1989/PyTorch-Encoding/)
* 由于原作者没有提供cityscapes数据集训练的模型权重文件，因时间原因，复现在该数据集上只迭代20000次，次数太少，miou精度不够


## Paddle版本代码运行依赖
* PaddlePaddle >= 2.1
* Python = 3.7

## Pytorch版本代码运行步骤
* 原作者说明 [链接](https://hangzhang.org/PyTorch-Encoding/notes/compile.html)


## Citation
If you find my project useful in your research, please consider citing:

```latex
@misc{
    author={Zhenglai Wang},
    howpublished = {\url{https://github.com/PaddlePaddle/PaddleSeg}},
    year={2021}
}
```
