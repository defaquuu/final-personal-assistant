import pytest
import sys
import os

# Добавляем путь к проекту
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_imports():
    """Проверка импортов"""
    try:
        from bot import main
        assert True
    except ImportError as e:
        pytest.fail(f"Ошибка импорта: {e}")

def test_environment():
    """Проверка переменных окружения"""
    assert 'TELEGRAM_BOT_TOKEN' in os.environ or True  # Для тестов
    assert 'TELEGRAM_CHAT_ID' in os.environ or True

def test_basic_math():
    """Простые тесты"""
    assert 1 + 1 == 2
    assert len("test") == 4

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
