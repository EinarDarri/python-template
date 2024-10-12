from __future__ import annotations
from collections import defaultdict

# should pass
def a(numb: int, b: str) -> None:
	"""
	some doc
	"""
	if numb:
		pass


def b(foo: str) -> str:
	"""
	some doc
	"""
	return foo


try:
	pass
except ValueError:
	pass


if __name__ == "__main__":
	b("Hello World")
	k = 3
	dic: dict[str, int] = defaultdict(int)


# should fail

# def c(numb: int, b) -> None:
# 	"""
# 	some doc
# 	"""
# 	if numb:
# 		return 1


# def Denni_Besti(foo: str) -> str:
# 	return foo


# try:
# 	pass
# except:
# 	pass


# if __name__ == "__main__":
# 	b("Hello World")
# 	k = 3
# 	dic: dict[str, int] = defaultdict(int)