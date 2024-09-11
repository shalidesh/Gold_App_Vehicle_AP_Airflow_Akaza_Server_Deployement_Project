import unittest
import requests

class TestPredictAPI(unittest.TestCase):
    def setUp(self):
        self.url = 'http://localhost:8443/predict'
        self.headers = {
            'Authorization': 'bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW4ifQ.JnAST4Q2VCLqy-raqX6pyiaNL_f9GiZKpDBn2-a2P9k',
            'Content-Type': 'application/json'
        }

    def test_case_1(self):
        payload = {
            "yom": "2015",
            "manufacture": "HONDA",
            "model": "DAA-RU3 VEZEL RS",
            "engine_capacity": "2000 CC",
            "fuel": "DIESEL",
            "transmission": "AUTOMATIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the HONDA test 01, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_2(self):
        payload = {
            "yom": "2017",
            "manufacture": "HONDA",
            "model": "DAA-GMA GRACE",
            "engine_capacity": "1500 CC",
            "fuel": "HYBRID",
            "transmission": "AUTOMATIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the HONDA test 02 , Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_3(self):
        payload = {
            "yom": "2015",
            "manufacture": "HONDA",
            "model": "FIT DBA-GE6",
            "engine_capacity": "1330 CC",
            "fuel": "PETROL",
            "transmission": "AUTOMATIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the HONDA test 03, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_4(self):
        payload = {
            "yom": "2011",
            "manufacture": "HONDA",
            "model": "DAA GP5 FIT - F",
            "engine_capacity": "1330 CC",
            "fuel": "PETROL",
            "transmission": "MANUAL"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the HONDA test 04, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_5(self):
        payload = {
            "yom": "2018",
            "manufacture": "HONDA",
            "model": "DAA-GP1 FIT",
            "engine_capacity": "1330 CC",
            "fuel": "DIESEL",
            "transmission": "MANUAL"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the HONDA test 05, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_6(self):
        payload = {
            "yom": "2018",
            "manufacture": "HONDA",
            "model": "Vezel RU3 Z",
            "engine_capacity": "1330 CC",
            "fuel": "HYBRID",
            "transmission": "TIPTRONIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the HONDA test 06, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_7(self):
        payload = {
            "yom": "2018",
            "manufacture": "HONDA",
            "model": "GH-CF3-ACCORD",
            "engine_capacity": "1330 CC",
            "fuel": "PETROL",
            "transmission": "TIPTRONIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the HONDA test 07, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_8(self):
        payload = {
            "yom": "2018",
            "manufacture": "HONDA",
            "model": "GH-CF3-ACCORD",
            "engine_capacity": "1330 CC",
            "fuel": "DIESEL",
            "transmission": "TIPTRONIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the HONDA test 08, Predicted_Price is {response_data['Predicted_Price']}")

    #########################Toyota####################

    def test_case_9(self):
        payload = {
            "yom": "2012",
            "manufacture": "TOYOTA",
            "model": "KDH222R-LEPNY (SFX-00)",
            "engine_capacity": "2000 CC",
            "fuel": "DIESEL",
            "transmission": "AUTOMATIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the TOYOTA test 01, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_10(self):
        payload = {
            "yom": "2017",
            "manufacture": "TOYOTA",
            "model": "DAA-NHP10 AQUA HYBRID",
            "engine_capacity": "1500 CC",
            "fuel": "HYBRID",
            "transmission": "AUTOMATIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the TOYOTA test 02 , Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_11(self):
        payload = {
            "yom": "2002",
            "manufacture": "TOYOTA",
            "model": "CAMRY",
            "engine_capacity": "1330 CC",
            "fuel": "PETROL",
            "transmission": "AUTOMATIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the TOYOTA test 03, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_12(self):
        payload = {
            "yom": "2000",
            "manufacture": "TOYOTA",
            "model": "COROLLA AE 121",
            "engine_capacity": "1330 CC",
            "fuel": "PETROL",
            "transmission": "MANUAL"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the TOYOTA test 04, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_13(self):
        payload = {
            "yom": "2010",
            "manufacture": "TOYOTA",
            "model": "HILUX LN 106",
            "engine_capacity": "1330 CC",
            "fuel": "DIESEL",
            "transmission": "MANUAL"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the TOYOTA test 05, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_14(self):
        payload = {
            "yom": "2015",
            "manufacture": "TOYOTA",
            "model": "AXIO",
            "engine_capacity": "1330 CC",
            "fuel": "HYBRID",
            "transmission": "TIPTRONIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the TOYOTA test 06, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_15(self):
        payload = {
            "yom": "2020",
            "manufacture": "TOYOTA",
            "model": "C-HR KOBA",
            "engine_capacity": "1330 CC",
            "fuel": "PETROL",
            "transmission": "TIPTRONIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the TOYOTA test 07, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_16(self):
        payload = {
            "yom": "2015",
            "manufacture": "TOYOTA",
            "model": "LAND CRUISER PRADO",
            "engine_capacity": "1330 CC",
            "fuel": "DIESEL",
            "transmission": "TIPTRONIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the TOYOTA test 08, Predicted_Price is {response_data['Predicted_Price']}")

    #########################NISSAN####################

    def test_case_17(self):
        payload = {
            "yom": "1995",
            "manufacture": "NISSAN",
            "model": "DAA-HFC26",
            "engine_capacity": "2000 CC",
            "fuel": "DIESEL",
            "transmission": "AUTOMATIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the NISSAN test 01, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_18(self):
        payload = {
            "yom": "2017",
            "manufacture": "NISSAN",
            "model": "X-TRAIL",
            "engine_capacity": "1500 CC",
            "fuel": "HYBRID",
            "transmission": "AUTOMATIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the NISSAN test 02 , Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_19(self):
        payload = {
            "yom": "2015",
            "manufacture": "NISSAN",
            "model": "VANNET LD20",
            "engine_capacity": "1330 CC",
            "fuel": "PETROL",
            "transmission": "AUTOMATIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the NISSAN test 03, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_20(self):
        payload = {
            "yom": "2000",
            "manufacture": "NISSAN",
            "model": "MARCH",
            "engine_capacity": "1330 CC",
            "fuel": "PETROL",
            "transmission": "MANUAL"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the NISSAN test 04, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_21(self):
        payload = {
            "yom": "2000",
            "manufacture": "NISSAN",
            "model": "BLUEBIRD",
            "engine_capacity": "1330 CC",
            "fuel": "DIESEL",
            "transmission": "MANUAL"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the NISSAN test 05, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_22(self):
        payload = {
            "yom": "2015",
            "manufacture": "NISSAN",
            "model": "AXIO",
            "engine_capacity": "1330 CC",
            "fuel": "HYBRID",
            "transmission": "TIPTRONIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the NISSAN test 06, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_23(self):
        payload = {
            "yom": "2018",
            "manufacture": "NISSAN",
            "model": "CLIPPER BUDY VAN",
            "engine_capacity": "1330 CC",
            "fuel": "PETROL",
            "transmission": "TIPTRONIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the NISSAN test 07, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_24(self):
        payload = {
            "yom": "2012",
            "manufacture": "NISSAN",
            "model": "X-TRAIL",
            "engine_capacity": "1330 CC",
            "fuel": "DIESEL",
            "transmission": "TIPTRONIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the NISSAN test 08, Predicted_Price is {response_data['Predicted_Price']}")

    #########################SUZUKI####################

    def test_case_25(self):
        payload = {
            "yom": "2002",
            "manufacture": "SUZUKI",
            "model": "ALTO - JAPAN",
            "engine_capacity": "2000 CC",
            "fuel": "DIESEL",
            "transmission": "AUTOMATIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the SUZUKI test 01, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_26(self):
        payload = {
            "yom": "2017",
            "manufacture": "SUZUKI",
            "model": "WAGON R FZ SAFETY",
            "engine_capacity": "1500 CC",
            "fuel": "HYBRID",
            "transmission": "AUTOMATIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the SUZUKI test 02 , Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_27(self):
        payload = {
            "yom": "2015",
            "manufacture": "SUZUKI",
            "model": "HUSTLER",
            "engine_capacity": "1330 CC",
            "fuel": "PETROL",
            "transmission": "AUTOMATIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the SUZUKI test 03, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_28(self):
        payload = {
            "yom": "2000",
            "manufacture": "SUZUKI",
            "model": "ALTO LXI 800CC",
            "engine_capacity": "1330 CC",
            "fuel": "PETROL",
            "transmission": "MANUAL"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the SUZUKI test 04, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_29(self):
        payload = {
            "yom": "2015",
            "manufacture": "SUZUKI",
            "model": "DAA-MK42S",
            "engine_capacity": "1330 CC",
            "fuel": "DIESEL",
            "transmission": "MANUAL"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the SUZUKI test 05, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_30(self):
        payload = {
            "yom": "2015",
            "manufacture": "SUZUKI",
            "model": "WAGON R STINGRAY",
            "engine_capacity": "1330 CC",
            "fuel": "HYBRID",
            "transmission": "TIPTRONIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the SUZUKI test 06, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_31(self):
        payload = {
            "yom": "2018",
            "manufacture": "SUZUKI",
            "model": "SWIFT",
            "engine_capacity": "1330 CC",
            "fuel": "PETROL",
            "transmission": "TIPTRONIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the SUZUKI test 07, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_32(self):
        payload = {
            "yom": "2018",
            "manufacture": "SUZUKI",
            "model": "CELERIO LXI MT",
            "engine_capacity": "1330 CC",
            "fuel": "DIESEL",
            "transmission": "TIPTRONIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the SUZUKI test 08, Predicted_Price is {response_data['Predicted_Price']}")

    #########################MICRO####################

    def test_case_33(self):
        payload = {
            "yom": "2008",
            "manufacture": "MICRO",
            "model": "KYRON",
            "engine_capacity": "2000 CC",
            "fuel": "DIESEL",
            "transmission": "AUTOMATIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the MICRO test 01, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_34(self):
        payload = {
            "yom": "2018",
            "manufacture": "MICRO",
            "model": "PANDA L.C 1.3",
            "engine_capacity": "1330 CC",
            "fuel": "PETROL",
            "transmission": "AUTOMATIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the MICRO test 03, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_35(self):
        payload = {
            "yom": "2019",
            "manufacture": "MICRO",
            "model": "MICRO TREND",
            "engine_capacity": "1330 CC",
            "fuel": "PETROL",
            "transmission": "MANUAL"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the MICRO test 04, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_36(self):
        payload = {
            "yom": "2009",
            "manufacture": "MICRO",
            "model": "ACTYON SPORTS",
            "engine_capacity": "1330 CC",
            "fuel": "DIESEL",
            "transmission": "MANUAL"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the MICRO test 05, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_37(self):
        payload = {
            "yom": "2018",
            "manufacture": "MICRO",
            "model": "REXTON270XDI",
            "engine_capacity": "1330 CC",
            "fuel": "PETROL",
            "transmission": "TIPTRONIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the MICRO test 07, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_38(self):
        payload = {
            "yom": "2018",
            "manufacture": "MICRO",
            "model": "REXTON270XDI",
            "engine_capacity": "1330 CC",
            "fuel": "DIESEL",
            "transmission": "TIPTRONIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the MICRO test 08, Predicted_Price is {response_data['Predicted_Price']}")

    #########################MITSUBISHI####################

    def test_case_39(self):
        payload = {
            "yom": "2008",
            "manufacture": "MITSUBISHI",
            "model": "MONTERO 3.2L GLS",
            "engine_capacity": "2000 CC",
            "fuel": "DIESEL",
            "transmission": "AUTOMATIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the MITSUBISHI test 01, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_40(self):
        payload = {
            "yom": "2008",
            "manufacture": "MITSUBISHI",
            "model": "OUTLANDER 2.4L PETROL",
            "engine_capacity": "1500 CC",
            "fuel": "HYBRID",
            "transmission": "AUTOMATIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the MITSUBISHI test 02 , Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_41(self):
        payload = {
            "yom": "2007",
            "manufacture": "MITSUBISHI",
            "model": "LANCER",
            "engine_capacity": "1330 CC",
            "fuel": "PETROL",
            "transmission": "AUTOMATIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the MITSUBISHI test 03, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_42(self):
        payload = {
            "yom": "2010",
            "manufacture": "MITSUBISHI",
            "model": "LANCER",
            "engine_capacity": "1330 CC",
            "fuel": "PETROL",
            "transmission": "MANUAL"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the MITSUBISHI test 04, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_43(self):
        payload = {
            "yom": "2000",
            "manufacture": "MITSUBISHI",
            "model": "CHARIOT",
            "engine_capacity": "1330 CC",
            "fuel": "DIESEL",
            "transmission": "MANUAL"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the MITSUBISHI test 05, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_44(self):
        payload = {
            "yom": "2018",
            "manufacture": "MITSUBISHI",
            "model": "ECLIPSE CROSS AWD",
            "engine_capacity": "1330 CC",
            "fuel": "PETROL",
            "transmission": "TIPTRONIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the MITSUBISHI test 07, Predicted_Price is {response_data['Predicted_Price']}")

    def test_case_45(self):
        payload = {
            "yom": "2018",
            "manufacture": "MITSUBISHI",
            "model": "ECLIPSE CROSS",
            "engine_capacity": "1330 CC",
            "fuel": "DIESEL",
            "transmission": "TIPTRONIC"
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertGreater(float(response_data['Predicted_Price']), -1)
        print(f"Passed the MITSUBISHI test 08, Predicted_Price is {response_data['Predicted_Price']}")


if __name__ == '__main__':
    unittest.main()
