import keyboard
from pynput.keyboard import Key, Controller
import time
import sys

# --- НАСТРОЙКИ ---
# Задержка перед выполнением команды (как ты просил, 1 секунда)
COMMAND_DELAY_SECONDS = 1 

# Создаем объект контроллера клавиатуры для имитации нажатий
kb_controller = Controller()

def send_media_key(media_key):
    """
    Имитирует нажатие и отпускание мультимедийной клавиши.
    
    :param media_key: Клавиша из pynput.keyboard.Key (например, Key.media_play_pause)
    """
    print(f"Ожидание {COMMAND_DELAY_SECONDS} сек перед отправкой команды...")
    time.sleep(COMMAND_DELAY_SECONDS) 
    
    try:
        # Нажатие клавиши
        kb_controller.press(media_key)
        # Небольшая задержка, чтобы ОС успела обработать
        time.sleep(0.05) 
        # Отпускание клавиши
        kb_controller.release(media_key)
        print(f"-> УСПЕШНО: Отправлена команда: {media_key}")
    except Exception as e:
        print(f"!!! ОШИБКА: Не удалось отправить команду {media_key}: {e}")

# --- ФУНКЦИИ УПРАВЛЕНИЯ СПОТИФАЙ (Используют твои горячие клавиши) ---

def custom_play_pause():
    """Горячая клавиша: Ctrl + Alt + Z. Переключает воспроизведение/паузу."""
    # Key.media_play_pause - стандартная мультимедийная клавиша Play/Pause
    send_media_key(Key.media_play_pause)

def custom_next_track():
    """Горячая клавиша: Ctrl + Alt + E. Переключает на следующий трек."""
    # Key.media_next - стандартная мультимедийная клавиша Next Track
    send_media_key(Key.media_next)

def custom_previous_track():
    """Горячая клавиша: Ctrl + Alt + Q. Переключает на предыдущий трек."""
    # Key.media_previous - стандартная мультимедийная клавиша Previous Track
    send_media_key(Key.media_previous)
    
def custom_volume_up():
    """Новая команда: Увеличивает громкость."""
    # Key.media_volume_up - стандартная мультимедийная клавиша Volume Up
    send_media_key(Key.media_volume_up)
    
def custom_volume_down():
    """Новая команда: Уменьшает громкость."""
    # Key.media_volume_down - стандартная мультимедийная клавиша Volume Down
    send_media_key(Key.media_volume_down)

def custom_mute_toggle():
    """Новая команда: Включает/выключает звук (Mute)."""
    # Key.media_mute - стандартная мультимедийная клавиша Mute
    send_media_key(Key.media_mute)

# --- РЕГИСТРАЦИЯ ГЛОБАЛЬНЫХ ГОРЯЧИХ КЛАВИШ ---

# 1. Play/Pause (Сохраняем твою комбинацию)
keyboard.add_hotkey('ctrl+alt+z', custom_play_pause)

# 2. Next Track (Сохраняем твою комбинацию)
keyboard.add_hotkey('ctrl+alt+e', custom_next_track)

# 3. Previous Track (Сохраняем твою комбинацию)
keyboard.add_hotkey('ctrl+alt+q', custom_previous_track)

# 4. Volume Up (Новая комбинация)
keyboard.add_hotkey('ctrl+alt+up', custom_volume_up)

# 5. Volume Down (Новая комбинация)
keyboard.add_hotkey('ctrl+alt+down', custom_volume_down)

# 6. Mute/Unmute (Новая комбинация)
keyboard.add_hotkey('ctrl+alt+m', custom_mute_toggle)


# --- ЗАПУСК ПРОГРАММЫ ---

print("="*60)
print("--- [Spotify Hotkeys Utility (Без API)] ---".center(60))
print("="*60)
print(f"Задержка перед командой: {COMMAND_DELAY_SECONDS} секунда(ы).")
print("\n🔥 Горячие клавиши (работают глобально):")
print("-" * 30)
print("1. Плей / Пауза:          Ctrl + Alt + Z")
print("2. Следующий трек:       Ctrl + Alt + E")
print("3. Предыдущий трек:      Ctrl + Alt + Q")
print("4. Увеличить громкость:  Ctrl + Alt + СТРЕЛКА ВВЕРХ")

print("-" * 30)
print("\nДля остановки программы нажмите Ctrl + C в этом окне консоли.")

try:
    # Блокировка программы для прослушивания событий клавиш
    keyboard.wait()
except KeyboardInterrupt:
    print("\nПрограмма остановлена пользователем.")
    sys.exit(0)
