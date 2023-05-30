from Series import *
from DataFrame import *

import unittest


class TestStringMethods(unittest.TestCase):
    def test_numerical_addition(self):
        sInt = SeriesInt("sales", [5, 3, 1, 10])
        sIntNone = SeriesInt("sales", [5, None, 1, 10])
        sFloat = SeriesFloat("price", [7.0, 3.5, 8.0, 6.0])
        outF = sFloat + sFloat
        outI = sInt + sInt
        outINone = sInt + sIntNone
        outI2 = sInt + 2
        outF2 = sFloat + 2.0

        print(outI)
        print(outINone)
        print(outI2)
        print(outF)
        print(outF2)


    def test_numerical_subtraction(self):
        sInt = SeriesInt("sales", [5, 3, 1, 10])
        sFloat = SeriesFloat("price", [7.0, 3.5, 8.0, 6.0])
        outF = sFloat - sFloat
        outI = sInt - sInt
        outI2 = sInt - 2
        outF2 = sFloat - 2.0

        print(outI)
        print(outI2)
        print(outF)
        print(outF2)


    def test_numerical_division(self):
        sInt = SeriesInt("sales", [5, 3, 1, 10])
        sFloat = SeriesFloat("price", [7.0, 3.5, 8.0, 6.0])
        outF = sFloat / sFloat
        outI = sInt / sInt
        outI2 = sInt / 2
        outF2 = sFloat / 2.0

        print(outI)
        print(outI2)
        print(outF)
        print(outF2)

    def test_numerical_multiplication(self):
        sInt = SeriesInt("sales", [5, 3, 1, 10])
        sFloat = SeriesFloat("price", [7.0, 3.5, 8.0, 6.0])
        outF = sFloat * sFloat
        outI = sInt * sInt
        outI2 = sInt * 2
        outF2 = sFloat * 2.0

        print(outI)
        print(outI2)
        print(outF)
        print(outF2)

    def test_numerical_less_than(self):
        sInt1 = SeriesInt("sales", [5, 3, 1, 10])
        sInt2 = SeriesInt("sales", [4, 6, 1, 10])
        sFloat1 = SeriesFloat("price", [6.0, 4.5, 8.0, 6.0])
        sFloat2 = SeriesFloat("price", [7.0, 3.5, 8.0, 6.0])
        outF = sFloat1 < sFloat2
        outI = sInt1 < sInt2
        outI2 = sInt1 < 2
        outF2 = sFloat1 < 2.0

        print(outI)
        print(outI2)
        print(outF)
        print(outF2)

    def test_numerical_greater_than(self):
        sInt1 = SeriesInt("sales", [5, 3, 1, 10])
        sInt2 = SeriesInt("sales", [4, 6, 1, 10])
        sFloat1 = SeriesFloat("price", [6.0, 4.5, 8.0, 6.0])
        sFloat2 = SeriesFloat("price", [7.0, 3.5, 8.0, 6.0])
        outF = sFloat1 > sFloat2
        outI = sInt1 > sInt2
        outI2 = sInt1 > 2
        outF2 = sFloat1 > 2.0

        print(outI)
        print(outI2)
        print(outF)
        print(outF2)

    def test_numerical_less_than_equal(self):
        sInt1 = SeriesInt("sales", [5, 3, 1, 10])
        sInt2 = SeriesInt("sales", [4, 6, 1, 10])
        sFloat1 = SeriesFloat("price", [6.0, 4.5, 8.0, 6.0])
        sFloat2 = SeriesFloat("price", [7.0, 3.5, 8.0, 6.0])
        outF = sFloat1 <= sFloat2
        outI = sInt1 <= sInt2
        outI2 = sInt1 <= 2
        outF2 = sFloat1 <= 2.0

        print(outI)
        print(outI2)
        print(outF)
        print(outF2)

    def test_numerical_greater_than_equal(self):
        sInt1 = SeriesInt("sales", [5, 3, 1, 10])
        sInt2 = SeriesInt("sales", [4, 6, 1, 10])
        sFloat1 = SeriesFloat("price", [6.0, 4.5, 8.0, 6.0])
        sFloat2 = SeriesFloat("price", [7.0, 3.5, 8.0, 6.0])
        outF = sFloat1 >= sFloat2
        outI = sInt1 >= sInt2
        outI2 = sInt1 >= 2
        outF2 = sFloat1 >= 2.0

        print(outI)
        print(outI2)
        print(outF)
        print(outF2)

    def test_numerical_not_equal(self):
        sInt1 = SeriesInt("sales", [5, 3, 1, 10])
        sInt2 = SeriesInt("sales", [4, 6, 1, 10])
        sFloat1 = SeriesFloat("price", [6.0, 4.5, 8.0, 6.0])
        sFloat2 = SeriesFloat("price", [7.0, 3.5, 8.0, 6.0])
        outF = sFloat1 != sFloat2
        outI = sInt1 != sInt2
        print(outI)
        print(outF)

    def test_equality(self):
        sInt = SeriesInt("sales", [5, 3, 1, 10])
        sBool = SeriesBool("sales", [False, False, True, False])
        sFloat = SeriesFloat("sales", [7.0, 3.5, 8.0, 6.0])
        sStr = SeriesString("price",  ["X4E", "T3B", "F8D", "C7X"])
        print(sFloat== sFloat)
        print(sInt == sInt)
        print(sStr == sStr)
        print(sBool == sBool)
        #print(sInt == sStr)

    def test_boolean(self):
        sBool1 = SeriesBool("sales", [False, False, True, True])
        sBool2 = SeriesBool("sales", [False, True, False, True])
        print(sBool1 & sBool2)
        print(sBool1 & True)
        print(sBool1 | sBool2)
        print(sBool1 | True)
        print(sBool1 ^ sBool2)
        print(sBool1 ^ True)
        print(~sBool1)

    def test_get_series(self):
        sStr = SeriesString("SKU", ["X4E", "T3B", "F8D", "C7X"])
        sBool = SeriesBool("taxed", [False, False, True, False])
        sOut = sStr[sBool]
        print(sOut)




    def test_default(self):
        sStr = SeriesString("SKU", ["X4E", "T3B", "F8D", "C7X"])
        sFloat = SeriesFloat("price", [7.0, 3.5, 8.0, 6.0])
        sFloat2 = SeriesFloat("price", [7.0, 3.5, 8.0, 6.0])
        sInt = SeriesInt("sales", [5, 3, 1, 10])
        sBool = SeriesBool("taxed", [False, False, True, False])
        df = DataFrame({"SKU": sStr, "price": sFloat, "sales": sInt, "taxed": sBool})
        price = df["price"]
        print(price)
        priceComp = (price + 5.0 > 10.0)
        print(priceComp)
        sales = df["sales"]
        salesComp = sales > 3
        print(sales)
        print(salesComp)
        taxed = df["taxed"]
        notTaxed = ~df["taxed"]
        print(taxed)
        print(notTaxed)

        print(priceComp & salesComp & notTaxed)

        result = df[priceComp & salesComp & notTaxed]["SKU"]
        print("result", result)
        result = df[(df["price"] + 5.0 > 10.0) & (df["sales"] > 3) & ~df["taxed"]]["SKU"]
        print("result", result)


if __name__ == '__main__':
    unittest.main()


#






