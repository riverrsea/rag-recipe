"""
RAG系统配置文件
"""

from dataclasses import asdict, dataclass
from typing import Dict, Any
import os


@dataclass
class RAGConfig:
	"""RAG系统配置类"""

	# 路径配置
	data_path: str = "../../data/C8/cook"
	# 向量索引
	index_save_path: str = "./vector_index"

	# 模型配置
	# 词嵌入模型
	embedding_model: str = "BAAI/bge-small-zh-v1.5"
	# 大模型
	llm_model: str = "kimi-k2-0711-preview"

	# 检索配置
	top_k: int = 3

	# 生成配置
	temperature: float = 0.1
	max_tokens: int = 2048

	base_url: str = ""

	@classmethod
	def from_dict(cls, config_dict: Dict[str, Any]) -> 'RAGConfig':
		"""从字典创建配置对象"""
		return cls(**config_dict)

	@classmethod
	def from_env(cls) -> 'RAGConfig':
		"""从环境变量创建配置对象"""
		return cls(
			data_path=os.getenv('DATA_PATH', cls.data_path),
			index_save_path=os.getenv('INDEX_SAVE_PATH', cls.index_save_path),
			embedding_model=os.getenv('EMBEDDING_MODEL', cls.embedding_model),
			llm_model=os.getenv('LLM_MODEL', cls.llm_model),
			top_k=int(os.getenv('TOP_K', cls.top_k)) if os.getenv(
				'TOP_K'
			) else 3,
			temperature=float(
				os.getenv('TEMPERATURE', cls.temperature)
			) if os.getenv(
				'TEMPERATURE'
			) else 0.1,
			max_tokens=int(
				os.getenv('MAX_TOKENS', cls.max_tokens)
			) if os.getenv(
				'max_tokens'
			) else 2048,
			base_url=os.getenv('BASE_URL', cls.base_url)
		)

	def to_dict(self) -> Dict[str, Any]:
		"""转换为字典"""
		return asdict(self)


# 默认配置实例
DEFAULT_CONFIG = RAGConfig()
