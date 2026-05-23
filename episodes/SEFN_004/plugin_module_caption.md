# SEFN Publishing Copy

## Title Candidates

- SEFN：给 Mamba 补上空间感
- Mamba 看得远，SEFN 负责看准局部
- 这个前馈模块，专门补 2D 空间信息

## Caption

SEFN 不是注意力，也不是频域分解。它把 Mamba 前的空间特征做成一个局部提示，再融合进 Mamba 后的前馈分支，用 `GELU(x1) * x2` 完成空间增强调制。

评论区打：SEFN  
拿 PDF 笔记、PyTorch 代码和架构图拆解。

## Hashtags

#深度学习 #Mamba #图像修复 #即插即用模块 #论文精读 #PyTorch
