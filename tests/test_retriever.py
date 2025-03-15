import pytest
from my_project import create_retriever

# 测试文档路径
TEST_PATH = "./data_kb"

def test_retriever_contains_keyword():
    test_query = "为我介绍一下2008年北京奥运会"
    expected_keyword = "奥运比赛"
    
    results = create_retriever(TEST_PATH, test_query)
    top_content = results[0].get_content() if results else ""
    
    assert expected_keyword in top_content, f"检索结果中未找到关键词 '{expected_keyword}'"

def test_retriever_empty_query():
    results = create_retriever(TEST_PATH, "")
    assert isinstance(results, list), "结果应该是列表类型"
