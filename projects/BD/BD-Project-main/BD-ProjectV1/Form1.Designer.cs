namespace BD_Final_Project
{
    partial class Form1
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
            Empresas = new Button();
            listBox1 = new ListBox();
            EmpresaNome = new TextBox();
            EmpresaEndereco = new TextBox();
            EmpresaTelefone = new TextBox();
            EmpresaEmail = new TextBox();
            EmpresaNIF = new TextBox();
            EmpresaAdicionar = new Button();
            label1 = new Label();
            label2 = new Label();
            label3 = new Label();
            label4 = new Label();
            label5 = new Label();
            EmpresaApagar = new Button();
            EmpresaEditar = new Button();
            EmpresaSearch = new TextBox();
            label6 = new Label();
            SearchBy = new ComboBox();
            NavioShow = new Button();
            Apply = new Button();
            SortBy = new Label();
            comboBox1 = new ComboBox();
            sort = new ComboBox();
            ShowNaviosButton = new Button();
            SuspendLayout();
            // 
            // Empresas
            // 
            Empresas.Location = new Point(46, 12);
            Empresas.Name = "Empresas";
            Empresas.Size = new Size(213, 48);
            Empresas.TabIndex = 0;
            Empresas.Text = "Empresas";
            Empresas.UseVisualStyleBackColor = true;
            Empresas.Click += ShowEmpresasButton_Click;
            // 
            // listBox1
            // 
            listBox1.FormattingEnabled = true;
            listBox1.ItemHeight = 15;
            listBox1.Location = new Point(46, 96);
            listBox1.Name = "listBox1";
            listBox1.Size = new Size(637, 274);
            listBox1.TabIndex = 1;
            listBox1.SelectedIndexChanged += listBox1_SelectedIndexChanged;
            // 
            // EmpresaNome
            // 
            EmpresaNome.Location = new Point(46, 417);
            EmpresaNome.Name = "EmpresaNome";
            EmpresaNome.Size = new Size(175, 23);
            EmpresaNome.TabIndex = 3;
            // 
            // EmpresaEndereco
            // 
            EmpresaEndereco.Location = new Point(498, 417);
            EmpresaEndereco.Name = "EmpresaEndereco";
            EmpresaEndereco.Size = new Size(175, 23);
            EmpresaEndereco.TabIndex = 5;
            // 
            // EmpresaTelefone
            // 
            EmpresaTelefone.Location = new Point(724, 417);
            EmpresaTelefone.Name = "EmpresaTelefone";
            EmpresaTelefone.Size = new Size(175, 23);
            EmpresaTelefone.TabIndex = 6;
            // 
            // EmpresaEmail
            // 
            EmpresaEmail.Location = new Point(953, 417);
            EmpresaEmail.Name = "EmpresaEmail";
            EmpresaEmail.Size = new Size(175, 23);
            EmpresaEmail.TabIndex = 7;
            // 
            // EmpresaNIF
            // 
            EmpresaNIF.Location = new Point(271, 417);
            EmpresaNIF.Name = "EmpresaNIF";
            EmpresaNIF.Size = new Size(175, 23);
            EmpresaNIF.TabIndex = 4;
            // 
            // EmpresaAdicionar
            // 
            EmpresaAdicionar.Location = new Point(46, 457);
            EmpresaAdicionar.Name = "EmpresaAdicionar";
            EmpresaAdicionar.Size = new Size(146, 62);
            EmpresaAdicionar.TabIndex = 8;
            EmpresaAdicionar.Text = "Adicionar Empresa";
            EmpresaAdicionar.UseVisualStyleBackColor = true;
            EmpresaAdicionar.Click += AddEmpresaButton_Click;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(46, 399);
            label1.Name = "label1";
            label1.Size = new Size(104, 15);
            label1.TabIndex = 9;
            label1.Text = "Nome da Empresa";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(502, 399);
            label2.Name = "label2";
            label2.Size = new Size(120, 15);
            label2.TabIndex = 10;
            label2.Text = "Endereço da Empresa";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(736, 399);
            label3.Name = "label3";
            label3.Size = new Size(115, 15);
            label3.TabIndex = 11;
            label3.Text = "Telefone da Empresa";
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Location = new Point(964, 399);
            label4.Name = "label4";
            label4.Size = new Size(100, 15);
            label4.TabIndex = 12;
            label4.Text = "Email da Empresa";
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.Location = new Point(271, 399);
            label5.Name = "label5";
            label5.Size = new Size(89, 15);
            label5.TabIndex = 13;
            label5.Text = "NIF da Empresa";
            // 
            // EmpresaApagar
            // 
            EmpresaApagar.Location = new Point(198, 457);
            EmpresaApagar.Name = "EmpresaApagar";
            EmpresaApagar.Size = new Size(146, 62);
            EmpresaApagar.TabIndex = 14;
            EmpresaApagar.Text = "Apagar Empresa";
            EmpresaApagar.UseVisualStyleBackColor = true;
            EmpresaApagar.Click += EmpresaApagar_Click;
            // 
            // EmpresaEditar
            // 
            EmpresaEditar.Location = new Point(350, 457);
            EmpresaEditar.Name = "EmpresaEditar";
            EmpresaEditar.Size = new Size(146, 62);
            EmpresaEditar.TabIndex = 15;
            EmpresaEditar.Text = "Editar Empresa";
            EmpresaEditar.UseVisualStyleBackColor = true;
            EmpresaEditar.Click += EmpresaEditar_Click;
            // 
            // EmpresaSearch
            // 
            EmpresaSearch.Location = new Point(724, 124);
            EmpresaSearch.Name = "EmpresaSearch";
            EmpresaSearch.Size = new Size(175, 23);
            EmpresaSearch.TabIndex = 16;
            EmpresaSearch.TextChanged += EmpresaSearch_TextChanged;
            // 
            // label6
            // 
            label6.AutoSize = true;
            label6.Location = new Point(724, 96);
            label6.Name = "label6";
            label6.Size = new Size(52, 15);
            label6.TabIndex = 17;
            label6.Text = "Procurar";
            // 
            // SearchBy
            // 
            SearchBy.FormattingEnabled = true;
            SearchBy.Items.AddRange(new object[] { "Nome", "NIF", "Endereço", "Telefone", "Email", "---" });
            SearchBy.Location = new Point(914, 124);
            SearchBy.Name = "SearchBy";
            SearchBy.Size = new Size(121, 23);
            SearchBy.TabIndex = 18;
            SearchBy.SelectedIndexChanged += SearchBy_SelectedIndexChanged;
            // 
            // NavioShow
            // 
            NavioShow.Location = new Point(284, 12);
            NavioShow.Margin = new Padding(2, 2, 2, 2);
            NavioShow.Name = "NavioShow";
            NavioShow.Size = new Size(213, 48);
            NavioShow.TabIndex = 19;
            NavioShow.Text = "Navios";
            NavioShow.UseVisualStyleBackColor = true;
            NavioShow.Click += NavioShow_Click;
            // 
            // Apply
            // 
            Apply.Location = new Point(724, 331);
            Apply.Margin = new Padding(2, 2, 2, 2);
            Apply.Name = "Apply";
            Apply.Size = new Size(95, 37);
            Apply.TabIndex = 20;
            Apply.Text = "Confirmar";
            Apply.UseVisualStyleBackColor = true;
            Apply.Click += Apply_Click;
            // 
            // SortBy
            // 
            SortBy.AutoSize = true;
            SortBy.Location = new Point(724, 193);
            SortBy.Margin = new Padding(2, 0, 2, 0);
            SortBy.Name = "SortBy";
            SortBy.Size = new Size(37, 15);
            SortBy.TabIndex = 21;
            SortBy.Text = "Filtrar";
            // 
            // comboBox1
            // 
            comboBox1.FormattingEnabled = true;
            comboBox1.Items.AddRange(new object[] { "Nome", "NIF", "Endereço", "Telefone", "Email", "---" });
            comboBox1.Location = new Point(724, 218);
            comboBox1.Name = "comboBox1";
            comboBox1.Size = new Size(121, 23);
            comboBox1.TabIndex = 22;
            // 
            // sort
            // 
            sort.FormattingEnabled = true;
            sort.Items.AddRange(new object[] { "Crescente", "Decrescente" });
            sort.Location = new Point(861, 218);
            sort.Margin = new Padding(2, 2, 2, 2);
            sort.Name = "sort";
            sort.Size = new Size(129, 23);
            sort.TabIndex = 23;
            // 
            // ShowNaviosButton
            // 
            ShowNaviosButton.Location = new Point(502, 457);
            ShowNaviosButton.Margin = new Padding(2, 2, 2, 2);
            ShowNaviosButton.Name = "ShowNaviosButton";
            ShowNaviosButton.Size = new Size(141, 62);
            ShowNaviosButton.TabIndex = 24;
            ShowNaviosButton.Text = "Navios Associados";
            ShowNaviosButton.UseVisualStyleBackColor = true;
            ShowNaviosButton.Click += ShowNaviosButton_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1156, 564);
            Controls.Add(ShowNaviosButton);
            Controls.Add(sort);
            Controls.Add(comboBox1);
            Controls.Add(SortBy);
            Controls.Add(Apply);
            Controls.Add(NavioShow);
            Controls.Add(SearchBy);
            Controls.Add(label6);
            Controls.Add(EmpresaSearch);
            Controls.Add(EmpresaEditar);
            Controls.Add(EmpresaApagar);
            Controls.Add(label1);
            Controls.Add(EmpresaAdicionar);
            Controls.Add(EmpresaEmail);
            Controls.Add(EmpresaTelefone);
            Controls.Add(EmpresaEndereco);
            Controls.Add(EmpresaNome);
            Controls.Add(EmpresaNIF);
            Controls.Add(listBox1);
            Controls.Add(label2);
            Controls.Add(label3);
            Controls.Add(label4);
            Controls.Add(label5);
            Controls.Add(Empresas);
            Name = "Form1";
            Text = "Form1";
            Load += Form1_Load;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button GoToForm2;
        private Button Empresas;
        private ListBox listBox1;
        private TextBox EmpresaNome;
        private TextBox EmpresaEndereco;
        private TextBox EmpresaTelefone;
        private TextBox EmpresaEmail;
        private TextBox EmpresaNIF;
        private Button EmpresaAdicionar;
        private Label label1;
        private Label label2;
        private Label label3;
        private Label label4;
        private Label label5;
        private Button EmpresaApagar;
        private Button EmpresaEditar;
        private TextBox EmpresaSearch;
        private Label label6;
        private ComboBox SearchBy;
        private Button NavioShow;
        private Button Apply;
        private Label SortBy;
        private ComboBox comboBox1;
        private ComboBox sort;
        private Button ShowNaviosButton;
    }
}
