from rag_pipeline_loader import rag_pipeline_setup

file_mapping = {
    "base_config_yaml_location": "../rag_pipeline_loader/configs/rag_config.yaml",
    "flavor": "langchain",
    "alias": "test_rag_pipeline"
}

obj = rag_pipeline_setup.LangChainRagPipeline(**file_mapping)