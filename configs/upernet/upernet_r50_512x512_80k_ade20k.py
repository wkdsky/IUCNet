_base_ = [
    # '../_base_/models/upernet_r50.py', '../_base_/datasets/ade20k.py',
    # '../_base_/default_runtime.py', '../_base_/schedules/schedule_80k.py'
    '../_base_/models/upernet_r50.py', '../_base_/datasets/drive.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_40k.py'
]
model = dict(
    decode_head=dict(num_classes=3), auxiliary_head=dict(num_classes=3))
