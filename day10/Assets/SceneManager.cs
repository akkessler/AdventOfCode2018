using System.Collections.Generic;
using UnityEngine;

public class SceneManager : MonoBehaviour
{

    string[] lines = System.IO.File.ReadAllLines("./Assets/input.txt");

    public Transform pointPrefab;

    public int startSecond = 0; // 10634

    private float elapsed;

    private List<Point> points;

    private bool reverse;

    void Start()
    {
        points = new List<Point>();
        elapsed = startSecond;
        foreach (string line in lines)
        {
            int positionIndexStart = line.IndexOf('<') + 1;
            int positionIndexEnd = line.IndexOf('>', positionIndexStart);
            string[] pos1 = line.Substring(positionIndexStart, positionIndexEnd - positionIndexStart).Split(',');
            float x1 = System.Convert.ToSingle(pos1[0]);
            float z1 = System.Convert.ToSingle(pos1[1]);
            Vector3 position = new Vector3(x1, 0f, -z1); // -z because problem statement says down is positive.

            int velocityIndexStart = line.IndexOf('<', positionIndexEnd) + 1;
            int velocityIndexEnd = line.IndexOf('>', velocityIndexStart);
            string[] pos2 = line.Substring(velocityIndexStart, velocityIndexEnd - velocityIndexStart).Split(',');
            float x2 = System.Convert.ToSingle(pos2[0]);
            float z2 = System.Convert.ToSingle(pos2[1]);
            Vector3 velocity = new Vector3(x2, 0f, -z2); // -z because problem statement says down is positive.

            Transform t = Instantiate(pointPrefab, position + (velocity * startSecond), Quaternion.identity);
            t.parent = transform;
            Point p = t.GetComponent<Point>();
            p.velocity = velocity;
            points.Add(p);
        }
    }

    void Update()
    {
        // TODO Could implement create logic to skip through most steps by checking overall distance of all points.
        // This would leave manual review only up to small section of steps (when height/width of point span is near its minimium)

        if (Input.GetKeyUp(KeyCode.Alpha1)) // For precise steps (only on key up)
        {
            MovePoints();
            Debug.Log(elapsed);
        }
        else if (Input.GetKey(KeyCode.Alpha2)) // Hold to step through points fast
        {
            MovePoints();
        }
        
        if (Input.GetKeyUp(KeyCode.Space)) // Toggle step direction
        {
            reverse = !reverse; 
        }
    }

    void MovePoints()
    {
        elapsed += reverse ? -1 : 1;
        foreach (Point p in points)
        {
            if (reverse) {
                p.StepBackward();
            }
            else
            {
                p.StepForward();
            }
        }
    }
}