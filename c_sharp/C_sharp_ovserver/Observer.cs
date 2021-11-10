using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace SampleAP
{
    interface Observer
    {
        void Update(Subject obj, object arg);
    }
}
