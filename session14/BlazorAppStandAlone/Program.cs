using BlazorAppStandAlone;
using BlazorAppStandAlone.Validators;
using FluentValidation;
using Microsoft.AspNetCore.Components.Web;
using Microsoft.AspNetCore.Components.WebAssembly.Hosting;

var builder = WebAssemblyHostBuilder.CreateDefault(args);
builder.RootComponents.Add<App>("#app");
builder.RootComponents.Add<HeadOutlet>("head::after");

builder.Services.AddScoped(sp => new HttpClient { BaseAddress = new Uri(builder.HostEnvironment.BaseAddress) });

// Add named HttpClient for Students API
builder.Services.AddHttpClient("StudentsAPI", client =>
{
    client.BaseAddress = new Uri("https://students.innopack.app/");
});

// Add FluentValidation services
builder.Services.AddValidatorsFromAssemblyContaining<StudentValidator>();

await builder.Build().RunAsync();
