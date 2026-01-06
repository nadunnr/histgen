model='histgen'
max_length=100
epochs=1
region_size=96
prototype_num=512

python main_test_AllinOne.py \
    --image_dir /home/nadun/wd/datasets/histgen_data/DINOv2_Features \
    --dataset_name wsi_report \
    --model_name $model \
    --max_seq_length $max_length \
    --threshold 10 \
    --batch_size 1 \
    --epochs $epochs \
    --step_size 1 \
    --topk 512 \
    --cmm_size 2048 \
    --cmm_dim 512 \
    --region_size $region_size \
    --prototype_num $prototype_num \
    --save_dir /home/nadun/wd/nadun/histgen/test_results \
    --step_size 1 \
    --gamma 0.8 \
    --seed 42 \
    --log_period 1000 \
    --load /home/nadun/wd/nadun/histgen/histgen_ckpt/model_best.pth \
    --beam_size 3 \
    --ann_path /home/nadun/wd/datasets/histgen_data/annotation_partial.json \
    # --ann_path /home/nadun/wd/nadun/histgen/dataset_annotations.json \
