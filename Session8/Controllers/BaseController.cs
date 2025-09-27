using StudentsAffairsWebAPI.Data.DbContexts;
using StudentsAffairsWebAPI.Data.Entities;
using System.Diagnostics;

namespace StudentsAffairsWebAPI;

[Route("api/[controller]")]
[ApiController]
public class BaseController<TEntity> : ControllerBase
    where TEntity : BaseEntity
{
    const int maxEntityCount = 15;
    protected readonly StudentsAffairsDbContext _studentsAffairsDbContext;
    public BaseController(StudentsAffairsDbContext studentsAffairsDbContext)
    {
        _studentsAffairsDbContext = studentsAffairsDbContext;

        if (_studentsAffairsDbContext.Set<TEntity>() is null || !_studentsAffairsDbContext.Set<TEntity>().Any())
            Fill(maxEntityCount);
    }
    public void Fill(int desiredCount)
    {
        Stopwatch stopwatch = new();
        stopwatch.Start();

        for (int i = 1; i <= desiredCount; i++)
        {
            TEntity? entity = Activator.CreateInstance<TEntity>();
            if (entity == null) continue;

            Type? type = typeof(TEntity);

            PropertyInfo? nameProperty = type.GetProperty("Name");
            if (nameProperty != null) nameProperty.SetValue(entity, $"{type.Name}{i}");

            PropertyInfo? ageProperty = type.GetProperty("Age");
            if (ageProperty != null) ageProperty.SetValue(entity, (byte)(18 + i));

            PropertyInfo? mobileProperty = type.GetProperty("Mobile");
            if (mobileProperty != null) mobileProperty.SetValue(entity, $"012345678{i}");

            _studentsAffairsDbContext.Set<TEntity>().Add(entity);
        }

        _studentsAffairsDbContext.SaveChanges();

        stopwatch.Stop();
        Console.ForegroundColor = ConsoleColor.Green;
        Console.WriteLine($"[Fill] Inserted {desiredCount} {typeof(TEntity).Name} in {stopwatch.ElapsedMilliseconds} ms");
        Console.ResetColor();
    }

    [HttpPost]
    public IActionResult Post([FromBody] TEntity entity)
    {
        Stopwatch stopwatch = new();
        stopwatch.Start();

        _studentsAffairsDbContext.Set<TEntity>().Add(entity);
        _studentsAffairsDbContext.SaveChanges();

        stopwatch.Stop();
        Console.ForegroundColor = ConsoleColor.Green;
        Console.WriteLine($"[Post] Inserted 1 {typeof(TEntity).Name} in {stopwatch.ElapsedMilliseconds} ms");
        Console.ResetColor();

        return Created();
    }

    [HttpGet]
    public IEnumerable<TEntity> GetAll()
    {
        return _studentsAffairsDbContext.Set<TEntity>().ToList() ?? new();
    }


    [HttpGet("{id}")]
    public IActionResult GetById([FromRoute] string id)
    {
        bool isParsedAsInt = int.TryParse(id, out int idParsed);
        if (!isParsedAsInt)
            return BadRequest($"The value {id} can't be parsed as int");

        try
        {
            TEntity? entityFromDb = _studentsAffairsDbContext.Set<TEntity>().FirstOrDefault(e => e.Id.Equals(idParsed));

            return Ok(entityFromDb);
        }
        catch (Exception exception)
        {
            return NotFound(exception.Message);
        }
    }

    [HttpPut]
    public IActionResult Update([FromBody] TEntity entity)
    {
        if (entity is null || string.IsNullOrEmpty(entity.Name)) throw new Exception("The entity can't be null or its name can't be empty");

        try
        {
            TEntity? entityFromDb = _studentsAffairsDbContext.Set<TEntity>().FirstOrDefault(e => e.Id.Equals(entity.Id));
            
            if (entityFromDb is null) return NotFound(entity);

            Type? type = typeof(TEntity);
            
            foreach (PropertyInfo propertyInfo in type.GetProperties())
            {
                if (!propertyInfo.CanWrite || propertyInfo.Name == "Id") continue;

                object? newValue = propertyInfo.GetValue(entity);
                propertyInfo.SetValue(entityFromDb, newValue);
            }

            _studentsAffairsDbContext.Set<TEntity>().Update(entityFromDb);
            _studentsAffairsDbContext.SaveChanges();

            return Ok(entityFromDb);
        }
        catch (Exception exception)
        {
            return NotFound(exception.Message);
        }
    }

    [HttpDelete("{id}")]
    public IActionResult Delete([FromRoute] string id)
    {
        bool isParsedAsInt = int.TryParse(id, out int idParsed);
        if (!isParsedAsInt)
            return BadRequest($"The value {id} can't be parsed as int");

        try
        {
            TEntity? toBeDeletedEntity = _studentsAffairsDbContext.Set<TEntity>().FirstOrDefault(e => e.Id.Equals(idParsed));

            if (toBeDeletedEntity is not null)
            {
                _studentsAffairsDbContext.Set<TEntity>().Remove(toBeDeletedEntity);
                _studentsAffairsDbContext.SaveChanges();
            }

            return Ok(toBeDeletedEntity);
        }
        catch (Exception exception)
        {
            return NotFound(exception.Message);
        }
    }
    [HttpDelete]
    public IActionResult Delete([FromBody] TEntity entity)
    {
        if (entity is null) throw new Exception("The entity can't be null");

        try
        {
            TEntity? entityFromDb = _studentsAffairsDbContext.Set<TEntity>().FirstOrDefault(e => e.Id.Equals(entity.Id));
            if (entityFromDb is null) return NotFound(entity);

            _studentsAffairsDbContext.Set<TEntity>().Remove(entityFromDb);
            _studentsAffairsDbContext.SaveChanges();

            return Ok(entity);
        }
        catch (Exception exception)
        {
            return NotFound(exception.Message);
        }
    }
}
