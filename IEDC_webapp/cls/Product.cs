namespace IEF_Database.cls
{
    public class Product
    {
        public Product()
        {
        }

        private int productId;
        private string name;
        private string productNumber;
        private string color;
        private string size;
        private string style;


        public virtual int ProductId
        {
            get { return productId; }
            set { productId = value; }
        }

        public virtual string Name
        {
            get { return name; }
            set { name = value; }
        }

        public virtual string ProductNumber
        {
            get { return productNumber; }
            set { productNumber = value; }
        }

        public virtual string Color
        {
            get { return color; }
            set { color = value; }
        }

        public virtual string Size
        {
            get { return size; }
            set { size = value; }
        }

        public virtual string Style
        {
            get { return style; }
            set { style = value; }
        }

        public Product(int productId, string name, string productNumber, string color, string size, string style)
        {
            this.productId = productId;
            this.name = name;
            this.productNumber = productNumber;
            this.color = color;
            this.size = size;
            this.style = style;
        }
    }
}