using System.Management;
using System.Text;

namespace SystemMonitorForm;

public partial class Form1 : Form
{
    public Form1()
    {
        InitializeComponent();
    }

    private void Form1_Load(object sender, EventArgs e)
    {
        LogStats();
        timer1.Start();
    }

    private void timer1_Tick(object sender, EventArgs e)
    {
        LogStats();
    }

    private void LogStats()
    {
        var stats = CollectSystemStats();
        textBoxLog.AppendText(stats + Environment.NewLine);
    }

    private string CollectSystemStats()
    {
        var stats = new StringBuilder();
        stats.AppendLine($"=== System Statistics at {DateTime.Now:yyyy-MM-dd HH:mm:ss} ===");

        // CPU Information
        using (var searcher = new ManagementObjectSearcher("root\\CIMV2", "SELECT * FROM Win32_Processor"))
        {
            foreach (ManagementObject obj in searcher.Get())
            {
                stats.AppendLine($"CPU Cores: {obj["NumberOfCores"]}");
                stats.AppendLine($"CPU Load: {obj["LoadPercentage"]}%");
                stats.AppendLine($"CPU Temperature: {GetCpuTemperature()}°C");
            }
        }

        // RAM Information
        using (var searcher = new ManagementObjectSearcher("root\\CIMV2", "SELECT * FROM Win32_ComputerSystem"))
        {
            foreach (ManagementObject obj in searcher.Get())
            {
                var totalRamGB = Convert.ToDouble(obj["TotalPhysicalMemory"]) / (1024 * 1024 * 1024);
                stats.AppendLine($"Total RAM: {totalRamGB:F2} GB");
            }
        }

        // Memory Usage
        using (var searcher = new ManagementObjectSearcher("root\\CIMV2", "SELECT * FROM Win32_OperatingSystem"))
        {
            foreach (ManagementObject obj in searcher.Get())
            {
                var freeRamGB = Convert.ToDouble(obj["FreePhysicalMemory"]) / (1024 * 1024);
                stats.AppendLine($"Free RAM: {freeRamGB:F2} GB");
            }
        }

        // Hard Drive Information
        using (var searcher = new ManagementObjectSearcher("root\\CIMV2", "SELECT * FROM Win32_DiskDrive"))
        {
            foreach (ManagementObject obj in searcher.Get())
            {
                stats.AppendLine($"HDD Model: {obj["Model"]}");
                stats.AppendLine($"HDD Serial: {obj["SerialNumber"]}");
                var sizeGB = Convert.ToDouble(obj["Size"]) / (1024 * 1024 * 1024);
                stats.AppendLine($"HDD Size: {sizeGB:F2} GB");
            }
        }

        stats.AppendLine(new string('-', 50));
        return stats.ToString();
    }

    private string GetCpuTemperature()
    {
        try
        {
            using (var searcher = new ManagementObjectSearcher(@"root\WMI", "SELECT * FROM MSAcpi_ThermalZoneTemperature"))
            {
                foreach (ManagementObject obj in searcher.Get())
                {
                    double temp = Convert.ToDouble(obj["CurrentTemperature"]);
                    return ((temp - 2732) / 10.0).ToString("F1");
                }
            }
        }
        catch
        {
            return "N/A";
        }
        return "N/A";
    }

    private void buttonPrintStatus_Click(object sender, EventArgs e)
    {
        LogStats();
    }

    private void buttonClearLog_Click(object sender, EventArgs e)
    {
        textBoxLog.Clear();
    }
}
