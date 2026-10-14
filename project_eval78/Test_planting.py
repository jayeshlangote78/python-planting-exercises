import unittest

from planting import row_capacity, reserve_row, planted_diameters


class TestRowCapacity(unittest.TestCase):
    def test_example_row(self):
        self.assertEqual(row_capacity(11.0, 2.0), 5)

    def test_exact_fit(self):
        self.assertEqual(row_capacity(10.0, 2.0), 5)

    def test_returns_whole_number(self):
        self.assertIsInstance(row_capacity(11.0, 2.0), int)

    def test_row_shorter_than_spacing(self):
        self.assertEqual(row_capacity(1.5, 2.0), 0)


class TestReserveRow(unittest.TestCase):
    def test_more_reserved_than_capacity(self):
        self.assertEqual(reserve_row(11.0, 2.0, [4, 6, 8, 10, 12, 14]), 5)

    def test_fewer_reserved_than_capacity(self):
        self.assertEqual(reserve_row(11.0, 2.0, [4, 6]), 2)

    def test_no_reservations(self):
        self.assertEqual(reserve_row(11.0, 2.0, []), 0)


class TestPlantedDiameters(unittest.TestCase):
    def test_example_row(self):
        self.assertEqual(
            planted_diameters(11.0, 2.0, [4, 6, 8, 10, 12, 14]),
            [4, 6, 8, 10, 12],
        )

    def test_keeps_order_when_all_fit(self):
        self.assertEqual(planted_diameters(20.0, 2.0, [9, 3, 7]), [9, 3, 7])

    def test_does_not_change_original_list(self):
        diameters = [4, 6, 8, 10, 12, 14]
        planted_diameters(11.0, 2.0, diameters)
        self.assertEqual(diameters, [4, 6, 8, 10, 12, 14])


if __name__ == "__main__":
    unittest.main()