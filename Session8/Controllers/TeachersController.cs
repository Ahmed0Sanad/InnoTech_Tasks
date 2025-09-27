using StudentsAffairsWebAPI.Data.DbContexts;
using StudentsAffairsWebAPI.Data.Entities;

namespace StudentsAffairsWebAPI;

[ApiController]
[Route("api/[controller]")]
public class TeachersController : BaseController<Teacher>
{
    public TeachersController(StudentsAffairsDbContext studentsAffairsDbContext) : base(studentsAffairsDbContext)
    {
    }
}
