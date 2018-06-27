import logging
from redis import StrictRedis
from info import constants


class Config(object):
    DEBUG = False
    # 连接数据库相关配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/news_ly"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 设置自动提交
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 非关系型数据库redis配置
    # 移至常量模块
    # REDIS_HOST = "127.0.0.1"
    # REDIS_PORT = 6379
    # 工程配置信息
    SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
    # flask_session的配置信息
    SESSION_TYPE = "redis"  # 指定 session 保存到 redis 中
    SESSION_USE_SIGNER = True  # 让 cookie 中的 session_id 被加密签名处理
    SESSION_REDIS = StrictRedis(host=constants.REDIS_HOST, port=constants.REDIS_PORT)  # 使用 redis 的实例
    PERMANENT_SESSION_LIFETIME = constants.SESSION_LIFETIME  # session 的有效期，单位是秒
    LOG_LEVEL = logging.DEBUG


class DevelopmentConfig(Config):
    """发展模式下的配置"""
    DEBUG = True
    LOG_LEVEL = logging.DEBUG


class ProductConfig(Config):
    """生产模式下的配置"""
    pass


config_dict = {
    "development":DevelopmentConfig,
    "product":ProductConfig
}