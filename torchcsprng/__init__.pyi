# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

from torch import Tensor, Generator

def supports_cuda() -> bool: ...

def create_random_device_generator(token: str = "") -> Generator: ...

def create_mt19937_generator(seed: int = 0): ...

def encrypt(input: Tensor, output: Tensor, key: Tensor, cipher, mode): ...

def decrypt(input: Tensor, output: Tensor, key: Tensor, cipher, mode): ...
