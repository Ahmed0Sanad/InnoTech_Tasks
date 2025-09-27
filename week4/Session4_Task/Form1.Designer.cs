namespace SystemMonitorForm;

partial class Form1
{
    private System.ComponentModel.IContainer components = null;
    private System.Windows.Forms.Timer timer1;
    private System.Windows.Forms.TextBox textBoxLog;
    private System.Windows.Forms.Button buttonPrintStatus;
    private System.Windows.Forms.Button buttonClearLog;

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
        this.components = new System.ComponentModel.Container();
        this.timer1 = new System.Windows.Forms.Timer(this.components);
        this.textBoxLog = new System.Windows.Forms.TextBox();
        this.buttonPrintStatus = new System.Windows.Forms.Button();
        this.buttonClearLog = new System.Windows.Forms.Button();
        this.SuspendLayout();
        // 
        // timer1
        // 
        this.timer1.Interval = 60000; // 1 minute
        this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
        // 
        // textBoxLog
        // 
        this.textBoxLog.Dock = System.Windows.Forms.DockStyle.Top;
        this.textBoxLog.Multiline = true;
        this.textBoxLog.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
        this.textBoxLog.Font = new System.Drawing.Font("Consolas", 10F);
        this.textBoxLog.ReadOnly = true;
        this.textBoxLog.BackColor = System.Drawing.Color.Black;
        this.textBoxLog.ForeColor = System.Drawing.Color.Lime;
        this.textBoxLog.Height = 370;
        // 
        // buttonPrintStatus
        // 
        this.buttonPrintStatus.Text = "Print Status";
        this.buttonPrintStatus.Location = new System.Drawing.Point(12, 380);
        this.buttonPrintStatus.Size = new System.Drawing.Size(120, 40);
        this.buttonPrintStatus.Click += new System.EventHandler(this.buttonPrintStatus_Click);
        // 
        // buttonClearLog
        // 
        this.buttonClearLog.Text = "Clear Console";
        this.buttonClearLog.Location = new System.Drawing.Point(140, 380);
        this.buttonClearLog.Size = new System.Drawing.Size(120, 40);
        this.buttonClearLog.Click += new System.EventHandler(this.buttonClearLog_Click);
        // 
        // Form1
        // 
        this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
        this.ClientSize = new System.Drawing.Size(800, 450);
        this.Controls.Add(this.buttonClearLog);
        this.Controls.Add(this.buttonPrintStatus);
        this.Controls.Add(this.textBoxLog);
        this.Name = "Form1";
        this.Text = "System Monitor";
        this.Load += new System.EventHandler(this.Form1_Load);
        this.ResumeLayout(false);
        this.PerformLayout();
    }

    #endregion
}
