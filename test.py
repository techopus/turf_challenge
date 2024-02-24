import unittest
from datetime import datetime, timedelta
from utils import calculate_health_score, schedule_maintenance, schedule_replacement

class TestPitchManagement(unittest.TestCase):


    def test_calculate_health_score(self):
        self.assertEqual(calculate_health_score(0, 'Natural', 'city', 'country'), 10)
        self.assertEqual(calculate_health_score(0, 'Artificial', 'city', 'country'), 10)
        self.assertEqual(calculate_health_score(0, 'Hybrid', 'city', 'country'), 10)

        self.assertEqual(calculate_health_score(3, 'Natural', 'city', 'country'), 8)
        self.assertEqual(calculate_health_score(4, 'Hybrid', 'city', 'country'), 8)
        self.assertEqual(calculate_health_score(6, 'Artificial', 'city', 'country'), 8)

        self.assertEqual(calculate_health_score(6, 'Natural', 'city', 'country'), 6)
        self.assertEqual(calculate_health_score(8, 'Hybrid', 'city', 'country'), 6)
        self.assertEqual(calculate_health_score(12, 'Artificial', 'city', 'country'), 6)

        self.assertEqual(calculate_health_score(9, 'Natural', 'city', 'country'), 4)
        self.assertEqual(calculate_health_score(12, 'Hybrid', 'city', 'country'), 4)
        self.assertEqual(calculate_health_score(18, 'Artificial', 'city', 'country'), 4)

        self.assertEqual(calculate_health_score(12, 'Natural', 'city', 'country'), 2)
        self.assertEqual(calculate_health_score(16, 'Hybrid', 'city', 'country'), 2)
        self.assertEqual(calculate_health_score(24, 'Artificial', 'city', 'country'), 2)

        self.assertEqual(calculate_health_score(15, 'Natural', 'city', 'country'), 0)
        self.assertEqual(calculate_health_score(20, 'Hybrid', 'city', 'country'), 0)
        self.assertEqual(calculate_health_score(30, 'Artificial', 'city', 'country'), 0)

    def test_schedule_maintenance(self):
        last_maintenance_date = datetime.now() - timedelta(hours=48)
        maintenance_date = schedule_maintenance(last_maintenance_date, 8, 'Natural')
        self.assertEqual(maintenance_date, last_maintenance_date + timedelta(hours=36))

        last_maintenance_date = datetime.now() - timedelta(hours=24)
        maintenance_date = schedule_maintenance(last_maintenance_date, 8, 'Hybrid')
        self.assertEqual(maintenance_date, last_maintenance_date + timedelta(hours=24))

        last_maintenance_date = datetime.now() - timedelta(hours=12)
        maintenance_date = schedule_maintenance(last_maintenance_date, 8, 'Artificial')
        self.assertEqual(maintenance_date, last_maintenance_date + timedelta(hours=12))

        last_maintenance_date = datetime.now() - timedelta(hours=48)
        maintenance_date = schedule_maintenance(last_maintenance_date, 8, 'Natural')
        self.assertEqual(maintenance_date, last_maintenance_date + timedelta(hours=36))

        last_maintenance_date = datetime.now() - timedelta(hours=24)
        maintenance_date = schedule_maintenance(last_maintenance_date, 8, 'Hybrid')
        self.assertEqual(maintenance_date, last_maintenance_date + timedelta(hours=24))

    
    def test_schedule_replacement(self):
        replacement_date = schedule_replacement(2)
        self.assertAlmostEqual(replacement_date, datetime.now() + timedelta(days=30), delta=timedelta(seconds=1))

        replacement_date = schedule_replacement(4)
        self.assertIsNone(replacement_date)

if __name__ == '__main__':
    unittest.main()
