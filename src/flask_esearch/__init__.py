from elasticsearch import Elasticsearch
from flask import Flask
from flask import _app_ctx_stack as stack


class ESearch:
    def __init__(self, app=None, **options):
        """
        Initializes the ESearch object
        Args:
            app: Flask object
            **options: dict options
        """
        self.app = app
        self.options = options
        if app is not None:
            self.init_app(self.app, **self.options)

    def init_app(self, app: Flask, **options) -> None:
        """
        Initializes the application with the extension.
        Creates and loads the settings from the settings configuration

        `ELASTICSEARCH_HOST` from the setting and it should be in
        the format of `str`. Defaults to localhost:9200 if nothing is set.

        `ELASTICSEARCH_HTTP_AUTH` from the setting and it should be in
        the format of `str`. E.g.: `username:password`

        Args:
            app: Flask application object
        """
        app.config.setdefault('ELASTICSEARCH_HOST', 'localhost:9200')
        app.config.setdefault('ELASTICSEARCH_HTTP_AUTH', None)

        self.options = options

        app.teardown_appcontext(self.teardown)

    def configure_app(self, context):
        """
        Validates the setting if exists and raise an Exception if not properly
        configured
        """
        hosts = context.app.config.get('ELASTICSEARCH_HOST')

        if not isinstance(hosts, (str, list)):
            raise ValueError(f"A __str__ or list is expected and not {type(hosts)}")
        elif isinstance(hosts, str):
            return [hosts]
        return hosts

    def __getattr__(self, item):
        context = stack.top

        if context is not None:
            if not hasattr(context, 'elasticsearch'):
                hosts = self.configure_app(context)
                auth = context.app.config.get('ELASTICSEARCH_HTTP_AUTH')
                context.elasticsearch = Elasticsearch(hosts=hosts, http_auth=auth, **self.options)

            return getattr(context.elasticsearch, item)
        raise RuntimeError("No Application Context")

    def teardown(self, exception):
        """
        Tears down when the application context ends
        """
        ctx = stack.top
        if hasattr(ctx, 'elasticsearch'):
            ctx.elasticsearch = None
