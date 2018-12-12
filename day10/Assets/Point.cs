using UnityEngine;

public class Point : MonoBehaviour
{

    public Vector3 velocity;

    void Start()
    {
        // velocity = Vector3.zero;
    }
    
    public void StepForward()
    {
        transform.position += velocity;
    }

    public void StepBackward()
    {
        transform.position -= velocity;
    }

}