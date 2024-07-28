from adapters import AutoAdapterModel


def get_model_summary(model_name, adapter_name=None, adapter_config="pfeiffer"):
    model = AutoAdapterModel.from_pretrained(model_name)
    model.add_adapter(adapter_name, config=adapter_config)
    model.set_active_adapters(adapter_name)

    print(model.adapter_summary())


if __name__ == "__main__":
    model_name = "LazarusNLP/IndoNanoT5-base"
    adapter_configs = [
        ("lora_r8", "lora[r=8]"),
        ("lora_r16", "lora[r=16]"),
        ("prefix_tuning_5", "prefix_tuning[prefix_length=5]"),
        ("prefix_tuning_50", "prefix_tuning[prefix_length=50]"),
        ("seq_bn_16", "seq_bn[reduction_factor=16]"),
        ("seq_bn_64", "seq_bn[reduction_factor=64]"),
        ("unipelt", "unipelt"),
    ]

    for adapter_name, adapter_config in adapter_configs:
        get_model_summary(model_name, adapter_name, adapter_config)
