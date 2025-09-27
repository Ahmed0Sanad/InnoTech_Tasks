namespace BlazorAppStandAlone.Components;
using System.Text.Json;
using System.Net.Http.Json;
using Microsoft.AspNetCore.Components;

public partial class Students
{

    private Student student = new();
    private List<Student> students = new List<Student>();
    private bool isEditing = false;
    private string? errorMessage;
    private bool isLoading = false;
    HttpClient client = new HttpClient();
   protected override async Task OnInitializedAsync()
    {
        await LoadStudents();
    }

    private async Task LoadStudents()
    {
        try
        {
            isLoading = true;
            errorMessage = null;
            
            List<Student>? response = await client.GetFromJsonAsync<List<Student>>(
            "https://students.innopack.app/api/students");


            if (response != null)
            {
                students = response;
            }
        }
        catch (Exception ex)
        {
            errorMessage = $"Error loading students: {ex.Message}";
        }
        finally
        {
            isLoading = false;
            StateHasChanged();
        }
    }

    private async Task HandleValidSubmit()
    {
        try
        {
            isLoading = true;
            errorMessage = null;

            if (isEditing)
            {
                // Update existing student (PUT)
                HttpResponseMessage response = await client.PutAsJsonAsync(
                    "https://students.innopack.app/api/students", student);
                if (response.IsSuccessStatusCode)
                {
                    // Update the student in the local list
                    var index = students.FindIndex(s => s.Id == student.Id);
                    if (index >= 0)
                    {
                        students[index] = JsonSerializer.Deserialize<Student>(JsonSerializer.Serialize(student))!;
                    }
                }
                else
                {
                    errorMessage = $"Error updating student: {response.StatusCode}";
                }
            }
            else
            {

                HttpResponseMessage response = await client.PostAsJsonAsync(
                       "https://students.innopack.app/api/students", student);

                if (response.IsSuccessStatusCode)
                {
                    // Add the student to the local list
                    students.Add(JsonSerializer.Deserialize<Student>(JsonSerializer.Serialize(student))!);
                }
                else
                {
                    errorMessage = $"Error creating student: {response.StatusCode}";
                }
            }

            // Reset form
            ResetForm();
        }
        catch (Exception ex)
        {
            errorMessage = $"Error submitting form: {ex.Message}";
        }
        finally
        {
            isLoading = false;
            StateHasChanged();
        }
    }

    private void EditStudent(Student toBeEditedStudent)
    {
        student = JsonSerializer.Deserialize<Student>(JsonSerializer.Serialize(toBeEditedStudent))!;
        isEditing = true;
        StateHasChanged();
    }

    private void ResetForm()
    {
        student = new Student();
        isEditing = false;
    }

}