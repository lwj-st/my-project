from lazyllm import Retriever, Document

def create_retriever(path: str, query: str):
    """
    创建并执行检索
    
    Args:
        path (str): 文档的绝对路径
        query (str): 查询语句
        
    Returns:
        list: 检索结果
    """
    doc = Document(path)
    retriever = Retriever(doc, group_name="CoarseChunk", similarity="bm25_chinese", topk=3)
    return retriever(query)

