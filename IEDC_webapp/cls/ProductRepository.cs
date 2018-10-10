using System.Collections.Generic;
namespace IEF_Database.cls
{
    public class ProductRepository
    {


        public static IList<Product> GetProducts()
        {
            IList<Product> products = new List<Product>
                                          {
                                              new Product(1, "Coke", "Abc100","Red","s","Fasion"),
                                              new Product(2, "Pepsi", "Abc200","blue","xl","B"),
                                             
                                          };
            return products;
        }
    }
}