namespace BD_Final_Project
{
    partial class Form2
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            listBox2 = new ListBox();
            label6 = new Label();
            comboBox1 = new ComboBox();
            Empresas = new Button();
            NavioShow = new Button();
            SearchBox = new TextBox();
            SortBox = new Label();
            comboBox2 = new ComboBox();
            sort = new ComboBox();
            Apply = new Button();
            AddNavio = new Button();
            NavioID = new TextBox();
            NavioNome = new TextBox();
            NavioCapacidade = new TextBox();
            NavioNIFEmpresa = new TextBox();
            label1 = new Label();
            label2 = new Label();
            label3 = new Label();
            label4 = new Label();
            SuspendLayout();
            // 
            // listBox2
            // 
            listBox2.FormattingEnabled = true;
            listBox2.ItemHeight = 25;
            listBox2.Location = new Point(66, 160);
            listBox2.Margin = new Padding(4, 5, 4, 5);
            listBox2.Name = "listBox2";
            listBox2.Size = new Size(908, 454);
            listBox2.TabIndex = 1;
            listBox2.SelectedIndexChanged += listBox1_SelectedIndexChanged;
            // 
            // label6
            // 
            label6.AutoSize = true;
            label6.Location = new Point(1034, 160);
            label6.Margin = new Padding(4, 0, 4, 0);
            label6.Name = "label6";
            label6.Size = new Size(78, 25);
            label6.TabIndex = 17;
            label6.Text = "Procurar";
            label6.Click += label6_Click;
            // 
            // comboBox1
            // 
            comboBox1.FormattingEnabled = true;
            comboBox1.Items.AddRange(new object[] { "ID", "Nome", "Capacidade (Toneladas)", "NIF da Empresa" });
            comboBox1.Location = new Point(1306, 207);
            comboBox1.Margin = new Padding(4, 5, 4, 5);
            comboBox1.Name = "comboBox1";
            comboBox1.Size = new Size(171, 33);
            comboBox1.TabIndex = 18;
            comboBox1.SelectedIndexChanged += comboBox1_SelectedIndexChanged;
            // 
            // Empresas
            // 
            Empresas.Location = new Point(66, 25);
            Empresas.Margin = new Padding(4, 5, 4, 5);
            Empresas.Name = "Empresas";
            Empresas.Size = new Size(304, 80);
            Empresas.TabIndex = 19;
            Empresas.Text = "Empresas";
            Empresas.UseVisualStyleBackColor = true;
            // 
            // NavioShow
            // 
            NavioShow.Location = new Point(402, 25);
            NavioShow.Name = "NavioShow";
            NavioShow.Size = new Size(304, 80);
            NavioShow.TabIndex = 20;
            NavioShow.Text = "Navios";
            NavioShow.UseVisualStyleBackColor = true;
            NavioShow.Click += NavioShow_Click;
            // 
            // SearchBox
            // 
            SearchBox.Location = new Point(1034, 209);
            SearchBox.Name = "SearchBox";
            SearchBox.Size = new Size(245, 31);
            SearchBox.TabIndex = 21;
            // 
            // SortBox
            // 
            SortBox.AutoSize = true;
            SortBox.Location = new Point(1034, 317);
            SortBox.Name = "SortBox";
            SortBox.Size = new Size(56, 25);
            SortBox.TabIndex = 22;
            SortBox.Text = "Filtrar";
            // 
            // comboBox2
            // 
            comboBox2.FormattingEnabled = true;
            comboBox2.Items.AddRange(new object[] { "ID", "Nome", "Capacidade (Toneladas)", "NIF da Empresa", "---" });
            comboBox2.Location = new Point(1034, 370);
            comboBox2.Margin = new Padding(4, 5, 4, 5);
            comboBox2.Name = "comboBox2";
            comboBox2.Size = new Size(171, 33);
            comboBox2.TabIndex = 23;
            // 
            // sort
            // 
            sort.FormattingEnabled = true;
            sort.Items.AddRange(new object[] { "Crescente", "Decrescente" });
            sort.Location = new Point(1231, 370);
            sort.Name = "sort";
            sort.Size = new Size(182, 33);
            sort.TabIndex = 24;
            // 
            // Apply
            // 
            Apply.Location = new Point(1034, 555);
            Apply.Name = "Apply";
            Apply.Size = new Size(149, 59);
            Apply.TabIndex = 25;
            Apply.Text = "Confirmar";
            Apply.UseVisualStyleBackColor = true;
            Apply.Click += Apply_Click;
            // 
            // AddNavio
            // 
            AddNavio.Location = new Point(66, 738);
            AddNavio.Name = "AddNavio";
            AddNavio.Size = new Size(228, 91);
            AddNavio.TabIndex = 26;
            AddNavio.Text = "Adicionar Navio";
            AddNavio.UseVisualStyleBackColor = true;
            AddNavio.Click += AddNavio_Click;
            // 
            // NavioID
            // 
            NavioID.Location = new Point(66, 681);
            NavioID.Name = "NavioID";
            NavioID.Size = new Size(150, 31);
            NavioID.TabIndex = 27;
            // 
            // NavioNome
            // 
            NavioNome.Location = new Point(277, 681);
            NavioNome.Name = "NavioNome";
            NavioNome.Size = new Size(150, 31);
            NavioNome.TabIndex = 28;
            // 
            // NavioCapacidade
            // 
            NavioCapacidade.Location = new Point(486, 681);
            NavioCapacidade.Name = "NavioCapacidade";
            NavioCapacidade.Size = new Size(197, 31);
            NavioCapacidade.TabIndex = 29;
            // 
            // NavioNIFEmpresa
            // 
            NavioNIFEmpresa.Location = new Point(763, 681);
            NavioNIFEmpresa.Name = "NavioNIFEmpresa";
            NavioNIFEmpresa.Size = new Size(180, 31);
            NavioNIFEmpresa.TabIndex = 30;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(66, 641);
            label1.Name = "label1";
            label1.Size = new Size(30, 25);
            label1.TabIndex = 31;
            label1.Text = "ID";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(277, 641);
            label2.Name = "label2";
            label2.Size = new Size(61, 25);
            label2.TabIndex = 32;
            label2.Text = "Nome";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(486, 641);
            label3.Name = "label3";
            label3.Size = new Size(197, 25);
            label3.TabIndex = 33;
            label3.Text = "Capacidade (Toneladas)";
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Location = new Point(763, 641);
            label4.Name = "label4";
            label4.Size = new Size(137, 25);
            label4.TabIndex = 34;
            label4.Text = "NIF da Empresa";
            label4.TextAlign = ContentAlignment.TopCenter;
            // 
            // Form2
            // 
            AutoScaleDimensions = new SizeF(10F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1651, 940);
            Controls.Add(label4);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(NavioNIFEmpresa);
            Controls.Add(NavioCapacidade);
            Controls.Add(NavioNome);
            Controls.Add(NavioID);
            Controls.Add(AddNavio);
            Controls.Add(Apply);
            Controls.Add(sort);
            Controls.Add(comboBox2);
            Controls.Add(SortBox);
            Controls.Add(SearchBox);
            Controls.Add(NavioShow);
            Controls.Add(Empresas);
            Controls.Add(comboBox1);
            Controls.Add(label6);
            Controls.Add(listBox2);
            Margin = new Padding(4, 5, 4, 5);
            Name = "Form2";
            Text = "Form2";
            Load += Form2_Load;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion
        private ListBox listBox2;
        private TextBox EmpresaSearch;
        private Label label6;
        private ComboBox comboBox1;
        private Button Empresas;
        private Button NavioShow;
        private TextBox SearchBox;
        private Label SortBox;
        private ComboBox comboBox2;
        private ComboBox sort;
        private Button Apply;
        private Button AddNavio;
        private TextBox NavioID;
        private TextBox NavioNome;
        private TextBox NavioCapacidade;
        private TextBox NavioNIFEmpresa;
        private Label label1;
        private Label label2;
        private Label label3;
        private Label label4;
    }
}
