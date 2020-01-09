cd ../sif
THEANO_FLAGS=mode=FAST_RUN,device=cpu,floatX=float32 python train.py $@