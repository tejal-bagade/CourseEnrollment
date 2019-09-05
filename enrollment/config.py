import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or '0058830f0e2e7f163d9c050f3d4d305a69b66391'
