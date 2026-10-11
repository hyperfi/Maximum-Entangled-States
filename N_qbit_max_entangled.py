# Copyright 2022 Abhishek
# SPDX-License-Identifier: Apache-2.0
#
# Maximum-Entangled-States: N_qbit_max_entangled.py
# Original implementation by Abhishek
# https://github.com/hyperfi/Maximum-Entangled-States
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# See the accompanying NOTICE file for attribution information.

def Gen_max_entangle(N):
    ''' The function Gen_max_entangle(N) return the N-qbit Quantum Circuit which is maximally entangled. '''
    import numpy as np
    from qiskit import QuantumCircuit
    qc = QuantumCircuit(N)
    qc.h(0)
    qc.barrier()


    M = int(np.log2(N))
    # M = math.ceil(np.log2(N))
    total_cover = 1
    layer_size = 1
    for i in range(M):
        control = 0
        target = layer_size
        for j in range(layer_size):
            # print(control,target)
            qc.cx(control,target)
            control+=1
            target+=1
        total_cover += layer_size
        layer_size = layer_size*2
        qc.barrier()

    # print(total_cover)
    if total_cover < N:
        # print('yes')
        control = total_cover-2
        target = total_cover
        remain = N - total_cover
        for j in range(remain):
            # print(control,target)
            qc.cx(control,target)
            control+=1
            target+=1
    return qc
