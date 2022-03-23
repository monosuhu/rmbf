if __name__ == "__main__":
	try:
		__import__("rmbf").make()
	except Exception as e:
		exit(str(e))
