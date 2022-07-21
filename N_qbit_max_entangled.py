def Gen_max_entangle(N):
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
