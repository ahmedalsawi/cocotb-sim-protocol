`timescale 1ns/1ps

module top #(
  parameter integer DATA_WIDTH = 4
) (
  input  logic unsigned [DATA_WIDTH-1:0] A,
  input  logic unsigned [DATA_WIDTH-1:0] B,
  output logic unsigned [DATA_WIDTH:0]   X
);

  assign X = A + B;

  // Dump waves
  initial begin
    $dumpfile("dump.vcd");
    $dumpvars(1, top);
  end

  logic x=1;
  initial begin
      x =0;
      $display($time, ":From SV");
      #10;
      $display($time, ":From SV");
      #10;
      x =1;
      $display($time, ":From SV");
      #10;
      $display($time, ":From SV");
  end

endmodule
