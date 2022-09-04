"""Classe para controle de Logs."""
import logging
import os
import sys
import json


class Logger:
    """Classe de Logger."""

    def __init__(self, provider_name: str = None):
        """Construtor da classe."""
        name = "graphql_study"
        self.logger = logging.getLogger(name)

        log_format = "%(asctime)-15s %(levelname)s: %(message)s"
        formatter = logging.Formatter(log_format)
        hdlr = logging.StreamHandler(sys.stdout)
        hdlr.setFormatter(formatter)
        self.logger.addHandler(hdlr)

        log_level = self.get_log_level()
        self.logger.setLevel(log_level)

    def get_log_level(self):
        log_level = os.environ.get("LOG_LEVEL", logging.INFO)
        if log_level == "INFO":
            return logging.INFO

        return logging.DEBUG

    def info(self, message, **kwargs):
        """Log message in Debug level.

        Args:
            message ():
            **kwargs ():
        """
        message = json.dumps(message, ensure_ascii=False)
        self.logger.info(message, **kwargs)

    def warning(self, message, **kwargs):
        """Logger para nivel WARNING.

        Args:
            message ():
            **kwargs ():
        """
        message = json.dumps(message, ensure_ascii=False)
        self.logger.warning(message, **kwargs)

    def success(self, message, **kwargs):
        """Logger para nivel SUCCESS.

        Args:
            message ():
            **kwargs ():
        """
        message = json.dumps(message, ensure_ascii=False)
        self.logger.info(message, **kwargs)

    def error(self, message, **kwargs):
        """Logger para nivel ERROR.

        Args:
            message ():
            **kwargs ():
        """
        message = json.dumps(message, ensure_ascii=False)
        self.logger.error(message, **kwargs)

    def critical(self, message, **kwargs):
        """Logger para nivel CRITICAL.

        Args:
            message ():
            **kwargs ():
        """
        self.logger.critical(message, **kwargs)

    def debug(self, message, **kwargs):
        """Logger para nivel ERROR.

        Args:
            message ():
            **kwargs ():
        """
        self.logger.debug(message, **kwargs)
