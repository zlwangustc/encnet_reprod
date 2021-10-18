import numpy as np
from reprod_log import ReprodDiffHelper

if __name__ == "__main__":
    diff_helper = ReprodDiffHelper()

    info1 = diff_helper.load_info("./npy/forward_paddle.npy")
    info2 = diff_helper.load_info("./npy/forward_pytorch.npy")
    path = "./log/forward_diff.log"

    info1 = diff_helper.load_info("./npy/loss_paddle.npy")
    info2 = diff_helper.load_info("./npy/loss_pytorch.npy")
    path = "./log/loss_diff.log"

    info1 = diff_helper.load_info("./npy/bp_align_paddle.npy")
    info2 = diff_helper.load_info("./npy/bp_align_pytorch.npy")
    path = "./log/bp_align_diff.log"

    diff_helper.compare_info(info1, info2)
    diff_helper.report(
        diff_method="mean", diff_threshold=1e-1, path=path)