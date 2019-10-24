import numpy as np


def mask_theta(theta):
    if theta.ndim != 1:
        raise Exception("Invalid theta format")

    mask = [1 for _ in range(len(theta))]
    mask[0] = 0
    mask = np.array(mask)

    return mask * theta


def l2_norm(theta):
    theta = mask_theta(theta)
    return theta**2


def l1_norm(theta):
    theta = mask_theta(theta)
    return np.abs(theta)
