namespace BlazorApp.Pages;

public partial class Counter
{
    private static int persistentCount = 0;
    [Parameter] public int InitialCount { get; set; } = 1;
    [Parameter] public int Step { get; set; } = 1;
    [Parameter] public RenderFragment? ChildContent { get; set; }
    [Parameter] public RenderFragment? HeaderContent { get; set; }

    protected override void OnInitialized()
    {
        base.OnInitialized();

        if (persistentCount == 0)
        {
            persistentCount = InitialCount;
        }
    }
    private void IncrementCount()
    {
        persistentCount += Step;
    }
}