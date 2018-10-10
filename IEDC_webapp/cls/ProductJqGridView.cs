using System;
using System.Collections.Generic;
using System.Text;

namespace IEF_Database.cls
{
    public class ProductJqGridView : JqGridView
    {
        public IList<Product> Products
        {
            get { return _products; }
            set { _products = value; }
        }

        private IList<Product> _products;
        public ProductJqGridView(int total, int page, IList<Product> products) : base(total, page)
        {
            _products = products;
        }

        public override string ToJson()
        {
            StringBuilder stringBuilder = new StringBuilder("{");
            stringBuilder.Append("total: " + SurrondWithQuote(1) + ", ");
            stringBuilder.Append("page: " + SurrondWithQuote(1) + ", ");
            stringBuilder.Append("records: " + SurrondWithQuote(Total) + ", ");
            stringBuilder.Append("  rows : [ ");
            for (int i = 0; i < Products.Count; i++)
            {
                stringBuilder.Append("{");

                stringBuilder.Append("id:" + SurrondWithQuote(i+1) + ", ");
                stringBuilder.Append("cell:[ ");
                stringBuilder.Append(SurrondWithQuote(Products[i].ProductId) + ", ");
                stringBuilder.Append(SurrondWithQuote(Products[i].Name) + ", ");
                stringBuilder.Append(SurrondWithQuote(Products[i].ProductNumber) + ", ");
                stringBuilder.Append(SurrondWithQuote(Products[i].Color) + ", ");
                stringBuilder.Append(SurrondWithQuote(Products[i].Size) + ", ");
                stringBuilder.Append(SurrondWithQuote(Products[i].Style));
                stringBuilder.Append(" ]");
                if (i == Products.Count - 1)
                {
                    stringBuilder.Append(" }");
                }
                else
                {
                    stringBuilder.Append(" },");
                }
            }
            stringBuilder.Append(" ]");
            stringBuilder.Append(" }");
            return stringBuilder.ToString();
        }
    }
}