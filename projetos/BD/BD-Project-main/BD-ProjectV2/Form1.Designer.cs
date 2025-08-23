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
            NavioShow = new Button();
            flowLayoutPanel1 = new FlowLayoutPanel();
            TrabalhadoresShow = new Button();
            EstatisticasSobreEmpresasShow = new Button();
            empresasPanel1 = new EmpresasPanel();
            naviosPanel1 = new NaviosPanel();
            loginPanel1 = new LoginPanel();
            flowLayoutPanel1.SuspendLayout();
            SuspendLayout();
            // 
            // Empresas
            // 
            Empresas.Location = new Point(3, 3);
            Empresas.Name = "Empresas";
            Empresas.Size = new Size(213, 60);
            Empresas.TabIndex = 0;
            Empresas.Text = "Empresas";
            Empresas.UseVisualStyleBackColor = true;
            Empresas.Click += ShowEmpresasButton_Click;
            // 
            // NavioShow
            // 
            NavioShow.Location = new Point(221, 2);
            NavioShow.Margin = new Padding(2);
            NavioShow.Name = "NavioShow";
            NavioShow.Size = new Size(213, 61);
            NavioShow.TabIndex = 19;
            NavioShow.Text = "Navios";
            NavioShow.UseVisualStyleBackColor = true;
            NavioShow.Click += ShowNaviosButton_Click;
            // 
            // flowLayoutPanel1
            // 
            flowLayoutPanel1.Controls.Add(Empresas);
            flowLayoutPanel1.Controls.Add(NavioShow);
            flowLayoutPanel1.Controls.Add(TrabalhadoresShow);
            flowLayoutPanel1.Controls.Add(EstatisticasSobreEmpresasShow);
            flowLayoutPanel1.Location = new Point(12, 12);
            flowLayoutPanel1.Name = "flowLayoutPanel1";
            flowLayoutPanel1.Size = new Size(979, 64);
            flowLayoutPanel1.TabIndex = 24;
            // 
            // TrabalhadoresShow
            // 
            TrabalhadoresShow.Location = new Point(438, 2);
            TrabalhadoresShow.Margin = new Padding(2);
            TrabalhadoresShow.Name = "TrabalhadoresShow";
            TrabalhadoresShow.Size = new Size(213, 61);
            TrabalhadoresShow.TabIndex = 20;
            TrabalhadoresShow.Text = "Trabalhadores";
            TrabalhadoresShow.UseVisualStyleBackColor = true;
            // 
            // EstatisticasSobreEmpresasShow
            // 
            EstatisticasSobreEmpresasShow.Location = new Point(655, 2);
            EstatisticasSobreEmpresasShow.Margin = new Padding(2);
            EstatisticasSobreEmpresasShow.Name = "EstatisticasSobreEmpresasShow";
            EstatisticasSobreEmpresasShow.Size = new Size(213, 61);
            EstatisticasSobreEmpresasShow.TabIndex = 21;
            EstatisticasSobreEmpresasShow.Text = "Estatísticas sobre Empresas";
            EstatisticasSobreEmpresasShow.UseVisualStyleBackColor = true;
            // 
            // empresasPanel1
            // 
            empresasPanel1.Location = new Point(12, 80);
            empresasPanel1.Name = "empresasPanel1";
            empresasPanel1.Size = new Size(1139, 478);
            empresasPanel1.TabIndex = 25;
            empresasPanel1.Visible = false;
            // 
            // naviosPanel1
            // 
            naviosPanel1.Location = new Point(15, 82);
            naviosPanel1.Name = "naviosPanel1";
            naviosPanel1.Size = new Size(1139, 478);
            naviosPanel1.TabIndex = 26;
            // 
            // loginPanel1
            // 
            loginPanel1.BackColor = SystemColors.InactiveCaption;
            loginPanel1.Location = new Point(4, 4);
            loginPanel1.Name = "loginPanel1";
            loginPanel1.Size = new Size(1147, 556);
            loginPanel1.TabIndex = 27;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1156, 564);
            Controls.Add(loginPanel1);
            Controls.Add(naviosPanel1);
            Controls.Add(empresasPanel1);
            Controls.Add(flowLayoutPanel1);
            Name = "Form1";
            Text = "Form1";
            Load += Form1_Load;
            flowLayoutPanel1.ResumeLayout(false);
            ResumeLayout(false);
        }

        #endregion

        private Button GoToForm2;
        private Button Empresas;
        private Button NavioShow;
        private FlowLayoutPanel flowLayoutPanel1;
        private EmpresasPanel empresasPanel1;
        private NaviosPanel naviosPanel1;
        private Button TrabalhadoresShow;
        private Button EstatisticasSobreEmpresasShow;
        private LoginPanel loginPanel1;
    }
}
