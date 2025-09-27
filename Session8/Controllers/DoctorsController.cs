using StudentsAffairsWebAPI.Data.DbContexts;
using StudentsAffairsWebAPI.Data.Entities;

namespace StudentsAffairsWebAPI;

[Route("api/[controller]")]
[ApiController]
public class DoctorsController : BaseController<Applicant>
{
    public DoctorsController(StudentsAffairsDbContext studentsAffairsDbContext) : base(studentsAffairsDbContext)
    {
    }
}
