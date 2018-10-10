namespace IEF_Database.cls
{
    public abstract class JqGridView
    {
        private readonly int _total;
        private readonly int _page;

        protected JqGridView(int total, int page)
        {
            _total = total;
            _page = page;
        }

        public int Total
        {
            get { return _total; }
        }

        public int Page
        {
            get { return _page; }
        }

        public abstract string ToJson();

        protected string SurrondWithQuote(string data)
        {
            return "'" + data + "'";
        }

        protected string SurrondWithQuote(int data)
        {
            return "'" + data + "'";
        }
    }
}