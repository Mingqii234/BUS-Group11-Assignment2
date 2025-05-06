from abc import ABC, abstractmethod
import random

class BaseDataGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass

class DailyDataGenerator(BaseDataGenerator):
    def generate(self):
        return [random.randint(100, 300) for _ in range(24)]

class WeeklyDataGenerator(BaseDataGenerator):
    def generate(self):
        return [random.randint(800, 1500) for _ in range(7)]

class MonthlyDataGenerator(BaseDataGenerator):
    def generate(self):
        return [random.randint(1000, 3000) for _ in range(30)]

class DataGeneratorFactory:
    @staticmethod
    def create(period: str) -> BaseDataGenerator:
        if period == 'daily':
            return DailyDataGenerator()
        if period == 'weekly':
            return WeeklyDataGenerator()
        if period == 'monthly':
            return MonthlyDataGenerator()
        raise ValueError("Invalid period. Choose 'daily', 'weekly', or 'monthly'.")
