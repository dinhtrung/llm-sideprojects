import os

from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.trace import set_tracer_provider
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai import Agent

os.environ['OTEL_EXPORTER_OTLP_ENDPOINT'] = 'http://localhost:4318'
exporter = OTLPSpanExporter()
span_processor = BatchSpanProcessor(exporter)
tracer_provider = TracerProvider()
tracer_provider.add_span_processor(span_processor)

set_tracer_provider(tracer_provider)
Agent.instrument_all()
# TODO: load the model from dotenv
provider = OpenAIProvider(base_url="http://localhost:8080/v1", api_key="no-need-for-local-interference")
# chat_model = OpenAIChatModel(provider=provider, model_name="unsloth/gemma-4-E4B-it-GGUF:Q4_K_M")
chat_model = OpenAIChatModel(provider=provider, model_name="Qwen/Qwen2.5-3B-Instruct-GGUF:Q4_K_M")
